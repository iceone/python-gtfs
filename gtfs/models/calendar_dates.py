# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('CalendarDate')
_fields = (
    'service_id',
    'date',
    'exception_type'
)


class CalendarDate(BaseModel('CalendarDate', _fields)):
    __filename__ = 'calendar_dates.txt'
    __required__ = _fields
