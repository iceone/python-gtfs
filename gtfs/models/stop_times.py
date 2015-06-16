# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('StopTime')
_fields = (
    'trip_id',
    'arrival_time',
    'departure_time',
    'stop_id',
    'stop_sequence',
    'stop_headsign',
    'pickup_type',
    'drop_off_type',
    'shape_dist_traveled',
    'timepoint'
)


class StopTime(BaseModel('StopTime', _fields)):
    __filename__ = 'stop_times.txt'
    __required__ = (
        'trip_id',
        'arrival_time',
        'departure_time',
        'stop_id',
        'stop_sequence'
    )