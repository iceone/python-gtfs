# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Calendar')
_fields = (
    'service_id',
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
    'start_date',
    'end_date'
)


class Calendar(BaseModel('Calendar', _fields)):
    __filename__ = 'calendar.txt'
    __required__ = _fields
