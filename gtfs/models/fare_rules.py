# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('FareRule')
_fields = (
    'fare_id',
    'route_id',
    'origin_id',
    'destination_id',
    'contains_id',

)


class FareRule(BaseModel('FareRule', _fields)):
    __filename__ = 'fare_rules.txt'
    __required__ = ('fare_id')
