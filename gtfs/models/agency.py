# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Agency')
_fields = (
    'agency_id',
    'agency_name',
    'agency_url',
    'agency_timezone',
    'agency_lang',
    'agency_phone',
    'agency_fare_url'
)


class Agency(BaseModel('Agency', _fields)):
    __filename__ = 'agency.txt'
    __required__ = (
        'agency_name',
        'agency_url',
        'agency_timezone'
    )