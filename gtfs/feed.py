# -*- coding: utf-8 -*-
"""
    gtfs.feed
    ~~~~~~~~~~~~~~~~

    Contains all logic of GTFS feed.
"""
import csv
import StringIO
import zipfile

from gtfs.utils.validators import (srange, valid_lang_tag, valid_timezone,
    valid_lang, valid_date, valid_hex, valid_currency, valid_time, valid_digit,
    valid_signed_int, valid_url, valid_coord, get)
from gtfs.models import (Agency, Calendar, CalendarDate, FareAttribute, Trip,
    FareRule, FeedInfo, Frequency, Route, Shape, StopTime, Stop, Transfer)


class ZipMixin(object):
    __required__ = ()
    __optional__ = ()

    def __init__(self, filename):
        self._filename = filename

    def submit(self):
        ready = True
        for field in self.__required__:
            field = '_{}'.format(field)

            if not hasattr(self, field):
                raise AttributeError('Unknown field')

            attr = getattr(self, field)
            ready &= bool(attr)

        if not ready:
            raise RuntimeError('Feed missing some required fields.')

        arch = zipfile.ZipFile(self._filename, 'w')
        for field in self.__required__ + self.__optional__:
            attr = getattr(self, '_{}'.format(field))

            if not attr:
                # empty optional filename
                continue

            csvfile = StringIO.StringIO()
            csvdata = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

            # writing header
            csvdata.writerow(attr[0].__fields__)

            for row in attr:
                csvdata.writerow(row)

            arch.writestr(attr[0].__filename__, ''.join(csvfile.buflist))
            csvfile.close()

        arch.close()


class Feed(ZipMixin):
    __required__ = (
        'agency',
        'stops',
        'stop_times',
        'routes',
        'trips',
        'calendar',
    )
    __optional__ = (
        'calendar_dates',
        'fare_attributes',
        'fare_rules',
        'feed_info',
        'frequencies',
        'shapes',
        'transfers'
    )

    def __init__(self, filename):
        super(Feed, self).__init__(filename)

        for attr in self.__required__ + self.__optional__:
            setattr(self, '_{}'.format(attr), [])

    def add_agency(self, *args):
        agency = Agency(*args)

        assert agency.agency_id not in get('agency_id', self._agency), 'Dup!'

        assert valid_url(agency.agency_url), 'Invalid agency URL'
        assert valid_timezone(agency.agency_timezone), 'Invalid timezone'

        if agency.agency_lang:
            assert valid_lang(agency.agency_lang), 'Invalid ISO 639-2 lang'

        if agency.agency_fare_url:
            assert valid_url(agency.agency_fare_url, scheme=1), 'Invalid URL'

        self._agency.append(agency)

    def add_calendar(self, *args):
        calendar = Calendar(*args)

        assert calendar.service_id not in get('service_id', self._calendar)

        assert calendar.monday in srange(2), 'Out of range'
        assert calendar.tuesday in srange(2), 'Out of range'
        assert calendar.wednesday in srange(2), 'Out of range'
        assert calendar.thursday in srange(2), 'Out of range'
        assert calendar.friday in srange(2), 'Out of range'
        assert calendar.saturday in srange(2), 'Out of range'
        assert calendar.sunday in srange(2), 'Out of range'
        assert valid_date(calendar.start_date), 'Invalid date format'
        assert valid_date(calendar.end_date), 'Invalid date format'

        self._calendar.append(calendar)

    def add_calendar_date(self, *args):
        calendar_date = CalendarDate(*args)

        service_ids = get('service_id', self._calendar_dates)
        dates = get('date', self._calendar_dates)

        assert (calendar_date.service_id, calendar_date.date) not in \
            zip(service_ids, dates), 'Dup!'

        assert valid_date(calendar_date.date), 'Invalid date format'
        assert calendar_date.exception_type in srange(1, 3), 'Out of range'

        self._calendar_dates.append(calendar_date)

    def add_fare_attribute(self, *args):
        fare_attribute = FareAttribute(*args)

        assert fare_attribute.fare_id not in \
            get('fare_id', self._fare_attributes), 'Dup!'

        assert valid_currency(fare_attribute.currency_type), 'Invalid ISO 4217'
        assert fare_attribute.payment_method in srange(2), 'Out of range'
        assert fare_attribute.transfers in srange(3), 'Out of range'

        self._fare_attributes.append(fare_attribute)

    def add_fare_rule(self, *args):
        fare_rule = FareRule(*args)

        assert fare_rule.fare_id in get('fare_id', self._fare_attributes)
        assert fare_rule.route_id in get('route_id', self._routes)
        assert fare_rule.origin_id in get('origin_id', self._stops)
        assert fare_rule.destination_id in get('destination_id', self._stops)
        assert fare_rule.contains_id in get('contains_id', self._stops)

        self._fare_rules.append(fare_rule)

    def add_feed_info(self, *args):
        feed_info = FeedInfo(*args)

        assert valid_url(feed_info.feed_publisher_url), 'Invalid URL'
        assert valid_lang_tag(feed_info.feed_lang), 'Invalid BCP 47 tag'

        if feed_info.feed_start_date:
            assert valid_date(feed_info.feed_start_date), 'Invalid date'
            assert valid_date(feed_info.feed_end_date), 'Invalid date'

        self._feed_info(*args)

    def add_frequencies(self, *args):
        frequency = Frequency(*args)

        assert frequency.trip_id in get('trip_id', self._trips)

        assert valid_time(frequency.start_time), 'Invalid time'
        assert valid_time(frequency.end_time), 'Invalid time'
        assert valid_digit(frequency.headway_secs), 'Invalid digit'

        if frequency.exact_times:
            assert frequency.exact_times in srange(2), 'Out of range'

        self._frequencies.append(frequency)

    def add_route(self, *args):
        route = Route(*args)

        assert route.route_id not in get('route_id', self._routes)
        # agency_id optional in agencies
        if route.agency_id:
            assert route.agency_id in get('agency_id', self._agency)

        assert route.route_type in xrange(8), 'Out of range'

        if route.route_url:
            assert valid_url(route.route_url), 'Invalid URL'

        if route.route_text_color:
            assert valid_hex(route.route_text_color), 'Invalid hex color'

        self._routes.append(route)

    def add_shape(self, *args):
        shape = Shape(*args)

        assert valid_coord(shape.shape_pt_lat), 'Invalid coord'
        assert valid_coord(shape.shape_pt_lon), 'Invalid coord'
        assert valid_signed_int(shape.shape_pt_sequence), 'Invalid int'

        if shape.shape_dist_traveled:
            assert valid_signed_int(shape.shape_dist_traveled), 'Invalid int'

        self._shapes.append(shape)

    def add_stop_time(self, *args):
        stop_time = StopTime(*args)

        #assert stop_time.trip_id in get('trip_id', self._trips)

        assert valid_time(stop_time.arrival_time), 'Invalid time: %s' % stop_time.arrival_time
        assert valid_time(stop_time.departure_time), 'Invalid time: %s' % stop_time.departure_time

        assert stop_time.stop_id in get('stop_id', self._stops)
        assert valid_signed_int(stop_time.stop_sequence), 'Invalid int'

        if stop_time.pickup_type:
            assert stop_time.pickup_type in xrange(4), 'Out of range'

        if stop_time.drop_off_type:
            assert stop_time.drop_off_type in xrange(4), 'Out of range'

        if stop_time.shape_dist_traveled:
            assert valid_signed_int(stop_time.shape_dist_traveled), 'Invalid int'

        if stop_time.timepoint:
            assert stop_time.timepoint in xrange(2), 'Out of range'

        self._stop_times.append(stop_time)

    def add_stop(self, *args):
        stop = Stop(*args)

        assert stop.stop_id not in get('stop_id', self._stops)

        assert valid_coord(stop.stop_lat), 'Invalid coord'
        assert valid_coord(stop.stop_lon), 'Invalid coord'

        if stop.stop_url:
            print ('STOP URL', stop.stop_url)
            assert valid_url(stop.stop_url), 'Invalid URL'

        if stop.location_type:
            assert stop.location_type in xrange(2), 'Out of range'

        if stop.stop_timezone:
            assert valid_timezone(stop.stop_timezone), 'Invalid timezone'

        if stop.wheelchair_boarding:
            assert stop.wheelchair_boarding in xrange(3), 'Out of range'

        self._stops.append(stop)

    def add_transfer(self, *args):
        transfer = Transfer(*args)

        stop_ids = get('stop_id', self._stops)
        assert transfer.from_stop_id in stop_ids
        assert transfer.to_stop_id in stop_ids

        assert transfer.transfer_type in xrange(4), 'Out of range'

        if transfer.min_transfer_time:
            assert valid_signed_int(transfer.min_transfer_time), 'Invalid int'

        self._transfers.append(transfer)

    def add_trip(self, *args):
        trip = Trip(*args)

        assert trip.route_id in get('route_id', self._routes)
        #assert trip.service_id in get('service_id', self._calendar)

        assert trip.trip_id not in get('trip_id', self._trips)

        if trip.direction_id:
            assert trip.direction_id in xrange(2), 'Out of range'

        if trip.shape_id:
            assert trip.shape_id in get('shape_id', self._shapes)

        if trip.wheelchair_accessible:
            assert trip.wheelchair_accessible in xrange(3), 'Out of range'

        if trip.bikes_allowed:
            assert trip.bikes_allowed in xrange(3), 'Out of range'

        self._trips.append(trip)
