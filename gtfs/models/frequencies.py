# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Frequency')
_fields = (
    'trip_id',
    'start_time',
    'end_time',
    'headway_secs',
    'exact_times'
)


class Frequency(BaseModel('Frequency', _fields)):
    __filename__ = 'frequencies.txt'
    __required__ = _fields[:-1]
