# -*- coding: utf-8 -*-

from gtfs import Feed


def main():
    feed = Feed('test.zip')

    # Create our Agency
    feed.add_agency(
        'id',
        'OITS',
        'http://my-site.ru/',
        'Asia/Yekaterinburg',
        'rus',
        '02',
        ''
    )

    # Create stops
    feed.add_stop(
        123,
        321,
        'Stop name',
        'Stop desc',
        '55.0',
        '65.0',
        '',
        '',
        1,
        0,
        '',
        ''
    )

    # Create routes
    feed.add_route(
        123,
        'id',
        'route short name',
        'route long name',
        'route descr',
        3,
        '',
        'ffffff',
        '000000'
    )

    # Create calendar for trips
    feed.add_calendar(
        333,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        '20150620',
        '20150621'
    )

    # Create trip
    feed.add_trip(
        123,
        333,
        111,
        'headsign',
        'short name',
        1,
        '',
        '',
        '',
        ''
    )

    # Create stop times
    feed.add_stop_time(
        111,
        '00:00:00',
        '00:00:10',
        123,
        1,
        '',
        '',
        '',
        '',
        ''
    )

    feed.submit()


if __name__ == '__main__':
    main()