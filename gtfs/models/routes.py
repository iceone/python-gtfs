# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Route')
_fields = (
    'route_id',
    'agency_id',
    'route_short_name',
    'route_long_name',
    'route_desc',
    'route_type',
    'route_url',
    'route_color',
    'route_text_color'
)


class Route(BaseModel('Route', _fields)):
    __filename__ = 'routes.txt'
    __required__ = (
        'route_id',
        'route_short_name',
        'route_long_name',
        'route_type'
    )