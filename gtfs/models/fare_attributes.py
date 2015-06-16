# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('FareAttribute')
_fields = (
    'fare_id',
    'price',
    'currency_type',
    'payment_method',
    'transfers',
    'transfer_duration'
)


class FareAttribute(BaseModel('FareAttribute', _fields)):
    __filename__ = 'fare_attributes.txt'
    __required__ = _fields[:-1]
