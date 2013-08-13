#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import calendar
import pytz
import dateutil.relativedelta
import dateutil.parser
from datetime import *

utc_timezone = pytz.UTC
china_timezone = pytz.timezone('Asia/Shanghai')

to_timestamp = lambda dt: calendar.timegm(dt.utctimetuple())
dthandler = lambda obj: to_timestamp(obj) if isinstance(obj, datetime) else obj
    
def stamp_time(message=None):
    text = u'Timestamped at <{0}>'.format(now())
    if message:
        text = u'{0}. {1}'.format(message, text)
    logging.info(text)
    
def now():
    return datetime.utcnow()
    
def now_in_timestamp():
    return to_timestamp(now())
    
def get_datetime_ago(*args, **kwargs):
    return now() - timedelta(*args,**kwargs)
    
def get_datetime_months_ago(monthspan):
    return now() - dateutil.relativedelta.relativedelta(months=monthspan)
    
def get_local_datetime(native_datetime, local_timezone=None):
    local_timezone = local_timezone or china_timezone
    return native_datetime.replace(tzinfo=utc_timezone).astimezone(local_timezone)
    
def extract_datetime(datetime_str):
    if not datetime_str or datetime_str == u'NaN': return None
    if type(datetime_str) is datetime: return datetime_str
    if type(datetime_str) is int or type(datetime_str) is float or type(datetime_str) is long:
        return datetime.utcfromtimestamp(int(datetime_str))
    try:
        return dateutil.parser.parse(datetime_str).astimezone(utc_timezone).replace(tzinfo=None)
    except ValueError:
        try:
            return datetime.utcfromtimestamp(int(datetime_str))
        except ValueError:
            logging.warning(u'Unable to parse datetime string <{0}>'.format(datetime_str))
            return None
    
def get_datetime_str_age_check(hourspan=1):
    latest = get_datetime_ago(hours=hourspan)
    def is_old_datetime_str(datetime_str):
        this_datetime = extract_datetime(datetime_str)
        return this_datetime < latest if this_datetime else False
    return is_old_datetime_str
    
def unpack_key(*args, **kwargs): # Legacy function
    return unpack_array_key(*args, **kwargs)
    
def unpack_array_key(key):
    defaults = [2013,12,31,23]
    args = [key[i] if len(key) > i else default for i,default in enumerate(defaults)]
    if args[1] == 2 and args[2] > 28: args[2] = 27
    try:
        datetime_obj = datetime(*args)
    except ValueError, e:
        args[2] -= 1 if args[1] != 2 else 28
        datetime_obj = datetime(*args)
    return datetime_obj
    
def unpack_key_to_timestamp(key):
    return to_timestamp(unpack_key(key))
