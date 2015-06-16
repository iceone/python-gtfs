# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Shape')
_fields = (
    'shape_id',
    'shape_pt_lat',
    'shape_pt_lon',
    'shape_pt_sequence',
    'shape_dist_traveled'
)


class Shape(BaseModel('Shape', _fields)):
    __filename__ = 'shapes.txt'
    __required__ = _fields[:-1]
