# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Trip')
_fields = (
    'route_id',
    'service_id',
    'trip_id',
    'trip_headsign',
    'trip_short_name',
    'direction_id',
    'block_id',
    'shape_id',
    'wheelchair_accessible',
    'bikes_allowed'
)


class Trip(BaseModel('Trip', _fields)):
    __filename__ = 'trips.txt'
    __required__ = (
        'route_id',
        'service_id',
        'trip_id'
    )