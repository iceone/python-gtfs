# -*- coding: utf-8 -*-
"""
    gtfs.feed
    ~~~~~~~~~~~~~~~~

    Contains all logic of GTFS feed.
"""
from gtfs.models import (Agency, Calendar, CalendarDate, FareAttribute, Trip,
    FareRule, FeedInfo, Frequency, Route, Shape, StopTime, Stop, Transfer)


class Feed(object):
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

    def __init__(self, zipfile):
        self._zipfile = zipfile

        for attr in self.__required__ + self.__optional__:
            setattr(self, '_{}'.format(attr), [])

    def add_agency(self, *args):
        agency = Agency(*args)

        # checks
        self._agency.append(agency)

    def add_calendar(self, *args):
        calendar = Calendar(*args)

        self._calendar.append(calendar)

    def add_calendar_date(self, *args):
        calendar_date = CalendarDate(*args)

        self._calendar_dates.append(calendar_date)

    def add_fare_attribute(self, *args):
        fare_attribute = FareAttribute(*args)

        self._fare_attributes.append(fare_attribute)

    def add_fare_rule(self, *args):
        fare_rule = FareRule(*args)

        self._fare_rules.append(fare_rule)

    def add_feed_info(self, *args):
        feed_info = FeedInfo(*args)

        self._feed_info(*args)

    def add_frequencies(self, *args):
        frequency = Frequency(*args)

        self._frequencies.append(frequency)

    def add_route(self, *args):
        route = Route(*args)

        self._routes.append(route)

    def add_shape(self, *args):
        shape = Shape(*args)

        self._shapes.append(shape)

    def add_stop_time(self, *args):
        stop_time = StopTime(*args)

        self._stop_times.append(stop_time)

    def add_stop(self, *args):
        stop = Stop(*args)

        self._stops.append(stop)

    def add_transfer(self, *args):
        transfer = Transfer(*args)

        self._transfers.append(transfer)

    def add_trip(self, *args):
        trip = Trip(*args)

        self._trips.append(trip)
