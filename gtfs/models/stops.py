# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Stop')
_fields = (
    'stop_id',
    'stop_code',
    'stop_name',
    'stop_desc',
    'stop_lat',
    'stop_lon',
    'zone_id',
    'stop_url',
    'location_type',
    'parent_station',
    'stop_timezone',
    'wheelchair_boarding',
)


class Stop(BaseModel('Stop', _fields)):
    __filename__ = 'stops.txt'
    __required__ = (
        'stop_id',
        'stop_name',
        'stop_lat',
        'stop_lon',
    )