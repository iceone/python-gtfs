# -*- coding: utf-8 -*-
from urlparse import urlparse
from datetime import datetime

from pytz import all_timezones_set as timezones
from pycountry import currencies
from iso639 import is_valid639_2
from language_tags import tags

_lang_tags = tags()

def get(attr, collection):
    return map(lambda x: getattr(x, attr), collection)

def srange(*args, **kwargs):
    return map(str, xrange(*args, **kwargs))


def valid_url(url, scheme=False):
    _url = urlparse(url)

    if scheme:
        print bool(_url.netloc) & bool(_url.scheme)

    return bool(_url.netloc)

def valid_timezone(tz):
    return tz in timezones

def valid_lang(lang):
    return is_valid639_2(lang)

def valid_lang_tag(tag):
    return _lang_tags.check(tag)

def valid_date(date):
    try:
        datetime.strptime(date, '%Y%m%d')
        return len(date) == 8
    except ValueError:
        return False

def valid_time(time):
    try:
        datetime.strptime(time, '%H:%M:%S')
        return len(time) == 8
    except ValueError:
        return False

def valid_digit(string):
    if hasattr(string, 'isdigit'):
        return string.isdigit()
    return False

def valid_currency(currency):
    return bool(currencies.indices['letter'].get(currency))

def valid_hex(string):
    try:
        int(string, 16)
        return len(string) == 6
    except ValueError:
        return False

def valid_coord(coord):
    try:
        return -180 <= float(coord) <= 180
    except ValueError:
        return False

def valid_signed_int(string):
    try:
        return int(string) > 0
    except ValueError:
        return False
