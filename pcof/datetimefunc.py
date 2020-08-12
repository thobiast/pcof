# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Date and time functions
"""


import datetime


##############################################################################
##############################################################################
# Unix epoch time conversion
##############################################################################
##############################################################################


def epoch_time_to_human(epoch, *, date_format="%c", utc="no"):  # pragma: no cover
    """
    Convert a unix epoch time to human format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments:
        epoch          (int): unix epoch time (timestamp)

    Keyword arguments (opt):
        date_format    (str): strftime format to show the epoch time
                              default is '%c' (Locale’s appropriate
                              date and time representation)
        utc         (yes/no): If unix epoch time in UTC timezone
                              default is no

    Example:
    >>> epoch_time_to_human(1530324373,date_format='%m%d%Y %H:%M:%S',utc='yes')
    '06302018 02:06:13'
    >>> epoch_time_to_human(1530324373) # doctest: +SKIP
    'Fri Jun 29 23:06:13 2018'
    >>> epoch_time_to_human(1530324373, utc='yes') # doctest: +SKIP
    'Sat Jun 30 02:06:13 2018'
    """
    if not isinstance(epoch, int):
        raise TypeError("epoch time must be int")

    if utc == "yes":
        return datetime.datetime.utcfromtimestamp(epoch).strftime(date_format)

    return datetime.datetime.fromtimestamp(epoch).strftime(date_format)


def epoch_time_now(*, utc="no"):
    """
    Return current date and time in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments:
        utc         (yes/no): If returns unix epoch time in UTC timezone
                              default is no
    Example:
    >>> epoch_time_now() # doctest: +SKIP
    1530325275
    """
    if utc == "yes":
        return int(datetime.datetime.utcnow().timestamp())
    elif utc == "no":
        return int(datetime.datetime.now().timestamp())

    raise ValueError("error: epoch_time_now: utc is invalid")


def epoch_time_min_ago(minutes=5, *, utc="no"):
    """
    Return current date and time less x minutes in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        minutes        (int): Number of minutes ago to return unix timestamp
                        default is 5 minutes

    Keyword arguments (opt):
        utc         (yes/no): If unix epoch time in UTC timezone
                              default is no
    Example:
    >>> epoch_time_min_ago() # doctest: +SKIP
    1530325377
    >>> epoch_time_min_ago(30) # doctest: +SKIP
    1530323879
    """
    if not isinstance(minutes, int):
        raise TypeError("minutes must be int")

    return int(epoch_time_now(utc=utc) - (60 * minutes))


def epoch_time_hours_ago(hours=1, *, utc="no"):
    """
    Return current date and time with less x hours in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        hours        (int): Number of hours ago to return unix timestamp
                            default is 1 hour

    Keyword arguments (opt):
        utc       (yes/no): If unix epoch time in UTC timezone
                            default is no
    Example:
    >>> epoch_time_hours_ago() # doctest: +SKIP
    1530322279
    >>> epoch_time_hours_ago(8) # doctest: +SKIP
    1530297083
    """
    if not isinstance(hours, int):
        raise TypeError("hours must be int")

    return int(epoch_time_now(utc=utc) - (hours * 3600))


def epoch_time_days_ago(days=1, *, utc="no"):
    """
    Return current date and time with less x days in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        days         (int): Number of days ago to return unix timestamp
                            default is 1 day

    Keyword arguments (opt):
        utc       (yes/no): If unix epoch time in UTC timezone
                            default is no
    Example:
    >>> epoch_time_days_ago() # doctest: +SKIP
    1530239517
    >>> epoch_time_days_ago(7) # doctest: +SKIP
    1529721118
    """
    if not isinstance(days, int):
        raise TypeError("days must be int")

    return int(epoch_time_now(utc=utc) - (days * 24 * 3600))


##############################################################################
##############################################################################
# Date and Time conversion
##############################################################################
##############################################################################


def time_unit_conversion(
    number, *, from_unit, to_unit, precision=0, days_month=30, days_year=365
):
    """
    Convert number from a time unit to another time unit.

    Arguments:
        number             (int): number to convert

    Keyword arguments:
        from_unit    (seconds/minutes/hours/days/weeks/months/years):
                                  unit to convert from
        to_unit      (seconds/minutes/hours/days/weeks/months/years):
                                  unit to convert to

    Keyword arguments (opt):
        precision          (int): number of digits after the decimal point
                                  (default 0)
        days_month   (int/float): number of days in each month
                                  (default 30)
        days_year    (int/float): number of days in each year
                                  (default 365)

    Return:
        number converted to new unit

    Example:
    >>> time_unit_conversion(3600, from_unit="seconds", to_unit="hours")
    '1'
    >>> time_unit_conversion(1400, from_unit="minutes", to_unit="days")
    '1'
    >>> time_unit_conversion(36, from_unit="hours", to_unit="days", precision=1)
    '1.5'
    >>> time_unit_conversion(90, from_unit="days", to_unit="months")
    '3'
    """
    in_seconds = {
        "seconds": 1,
        "minutes": 60,
        "hours": 60 * 60,
        "days": 60 * 60 * 24,
        "weeks": 60 * 60 * 24 * 7,
        "months": 60 * 60 * 24 * days_month,
        "years": 60 * 60 * 24 * days_year,
    }

    if any(key not in in_seconds for key in (from_unit, to_unit)):
        raise ValueError(
            "Invalid unit. It must be {}".format(", ".join(in_seconds.keys()))
        )

    if not isinstance(number, int):
        raise TypeError("number must be int")

    # convert to seconds
    sec = number * in_seconds[from_unit]
    # convert seconds to unit
    to_time = sec / in_seconds[to_unit]

    return "{0:.{prec}f}".format(to_time, prec=precision)


def seconds_to_human(seconds, *, unit=None):
    """
    Convert number in seconds to human format.

    Arguments:
        seconds      (int): Number of seconds

    Keyword arguments (opt):
        unit         (Months/Days/Hours/Minutes/Seconds):
                            Max unit used to convert

    Example:
    >>> seconds_to_human(300)
    '5 Minutes'
    >>> seconds_to_human(310)
    '5 Minutes, 10 Seconds'
    >>> seconds_to_human(10810)
    '3 Hours, 10 Seconds'
    >>> seconds_to_human(10810, unit='Minutes')
    '180 Minutes, 10 Seconds'
    >>> seconds_to_human(180072)
    '2 Days, 2 Hours, 1 Minutes, 12 Seconds'
    >>> seconds_to_human(5191272)
    '2 Months, 2 Hours, 1 Minutes, 12 Seconds'
    """
    # 1 year = 365 days (60 * 60 * 24 * 365)
    # 1 month = 30 days (60 * 60 * 24 * 30)
    # 1 day    (60 * 60 * 24)
    # 1 hour   (60 * 60)
    # 1 minute (60)
    # 1 second
    seconds_list = [
        ("Years", 31536000),
        ("Months", 2592000),
        ("Days", 86400),
        ("Hours", 3600),
        ("Minutes", 60),
        ("Seconds", 1),
    ]

    if not isinstance(seconds, int):
        raise TypeError("seconds must be int")

    if seconds == 0:
        return "0 Seconds"
    elif seconds < 0:
        raise TypeError("error: seconds_to_human: seconds must be greater than 0")

    # If unit is specified, fix seconds_list to contain only
    # granularity required and lower
    if unit:
        try:
            index = [a for a, b in enumerate(seconds_list) if b[0] == unit][0]
        except IndexError:
            raise TypeError("error: seconds_to_human: unit is invalid")
        seconds_list = seconds_list[index:]

    result = []
    # Loop over seconds_list
    for unit_name, unit_value_in_sec in seconds_list:
        # Check if the seconds can be divided by seconds in that granularity
        num_unit = seconds // unit_value_in_sec
        # If division would occur, decrease number of seconds and store
        # number of granularity and the granularity name in the result
        if num_unit:
            seconds -= num_unit * unit_value_in_sec
            result.append("{} {}".format(num_unit, unit_name))
    return ", ".join(result)


# vim: ts=4
