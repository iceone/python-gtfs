# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('Transfer')
_fields = (
    'from_stop_id',
    'to_stop_id',
    'transfer_type',
    'min_transfer_time'
)


class Transfer(BaseModel('Transfer', _fields)):
    __filename__ = 'transfers.txt'
    __required__ = _fields[:-1]
