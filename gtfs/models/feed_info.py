# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtfs.models import BaseModel

__all__ = ('FeedInfo')
_fields = (
    'feed_publisher_name',
    'feed_publisher_url',
    'feed_lang',
    'feed_start_date',
    'feed_end_date',
    'feed_version'
)


class FeedInfo(BaseModel('FeedInfo', _fields)):
    __filename__ = 'feed_info.txt'
    __required__ = _fields[:-2]
