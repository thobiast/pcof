# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Dependencies: pytz
"""


import datetime

import pytz


def convert_datetime_to_tz(*, date, date_fmt, from_tz="UTC", to_tz="America/Sao_Paulo"):
    """
    Convert a date to a specific timezone.

    Keyword arguments:

        date           (str): date to convert
        date_fmt       (str): format of the date to convert
        from_tz   (timezone): source timezone name (default: UTC)
        to_tz     (timezone): target timezone name (default: America/Sao_Paulo)

    Returns:
        datetime object with the target timezone defined.

    Example:
    # convert a date from utc to America/Sao_Paulo
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ")
    datetime.datetime(2019, 4, 26, 7, 38, 5,
                      tzinfo=<DstTzInfo 'America/Sao_Paulo' -03-1 day,
                      21:00:00 STD>)

    # convert date from America/Sao_Paulo to America/Los_Angeles
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ",
                               from_tz="America/Sao_Paulo",
                               to_tz="America/Los_Angeles")
    datetime.datetime(2019, 4, 26, 6, 38, 5, # doctest: +SKIP
                      tzinfo=<DstTzInfo 'America/Los_Angeles' PDT-1 day,
                      17:00:00 DST>)

    # Convert date from America/New_York to Asia/Dubai
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ",
                               from_tz="America/New_York",
                               to_tz="Asia/Dubai")
    datetime.datetime(2019, 4, 26, 18, 38, 5,
                      tzinfo=<DstTzInfo 'Asia/Dubai' +04+4:00:00 STD>)
    """
    # create datetime obj with date specified
    datetime_obj = datetime.datetime.strptime(date, date_fmt)
    # add timezone information to datetime obj
    datetime_obj_from = pytz.timezone(from_tz).localize(datetime_obj)
    # new datetime obj with target timezone
    datetime_obj_to = datetime_obj_from.astimezone(pytz.timezone(to_tz))

    return datetime_obj_to


# vim: ts=4
