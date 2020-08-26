# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Bytes calculator
"""


def bytes2human(size, *, unit="", precision=2, base=1024):
    """
    Convert number in bytes to human format.

    Arguments:
        size       (int): bytes to be converted

    Keyword arguments (opt):
        unit       (str): If it will convert bytes to a specific unit
                          'KB', 'MB', 'GB', 'TB', 'PB', 'EB'
        precision  (int): number of digits after the decimal point
        base       (int): 1000 - for decimal base
                          1024 - for binary base (it is the default)

    Returns:
        (int): number
        (str): unit ('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

    Example:
    >>> bytes2human(10)
    ('10.00', 'Bytes')
    >>> bytes2human(2048)
    ('2.00', 'KB')
    >>> bytes2human(27273042329)
    ('25.40', 'GB')
    >>> bytes2human(27273042329, precision=1)
    ('25.4', 'GB')
    >>> bytes2human(27273042329, unit='MB')
    ('26009.60', 'MB')
    """
    # validate parameters
    if not isinstance(precision, int):
        raise ValueError("precision is not a number")
    if not isinstance(base, int):
        raise ValueError("base is not a number")
    try:
        num = float(size)
    except ValueError:
        raise ValueError("value is not a number")

    suffix = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB"]

    # If it needs to convert bytes to a specific unit
    if unit:
        try:
            num = num / base ** suffix.index(unit)
        except ValueError:
            raise ValueError("Error: unit must be {}".format(", ".join(suffix[1:])))
        return "{0:.{prec}f}".format(num, prec=precision), unit

    # Calculate the greatest unit for the that size
    for counter, suffix_unit in enumerate(suffix):
        if num < base:
            return "{0:.{prec}f}".format(num, prec=precision), suffix_unit
        if counter == len(suffix) - 1:
            raise ValueError("value greater than the highest unit")
        num /= base


def human2bytes(size, unit, *, precision=2, base=1024):
    """
    Convert size from human to bytes.

    Arguments:
        size       (int): number
        unit       (str): converts from this unit to bytes
                          'KB', 'MB', 'GB', 'TB', 'PB', 'EB'

    Keyword arguments (opt):
        precision  (int): number of digits after the decimal point
                          default is 2
        base       (int): 1000 - for decimal base
                          1024 - for binary base (it is the default)

    Returns:
        (int) number in bytes

    Example:
    >>> human2bytes(10, 'GB')
    '10737418240.00'
    >>> human2bytes(10, 'GB', precision=0)
    '10737418240'
    >>> human2bytes(10, 'PB')
    '11258999068426240.00'

    """
    dic_power = {
        "KB": base,
        "MB": base ** 2,
        "GB": base ** 3,
        "TB": base ** 4,
        "PB": base ** 5,
        "EB": base ** 6,
        "ZB": base ** 7,
    }
    if unit not in dic_power:
        raise ValueError(
            "invalid unit. It must be {}".format(", ".join(dic_power.keys()))
        )

    try:
        num_bytes = float(size) * int(dic_power[unit])
    except ValueError:
        raise ValueError("value is not a number")

    return "{0:.{prec}f}".format(num_bytes, prec=precision)


def bandwidth_converter(
    number, *, from_unit, to_unit, from_time="seconds", to_time="seconds"
):
    """
    Bandwidth Calculator.

    Convert data rate from one unit to another.

    Arguments:
        number     (int): number to be converted

    Keyword arguments:
        from_unit  (str): convert from this data unit. Example:
                          (bps, Kbps, Mbps, Gbps... KB, KiB, MB, MiB...)
        to_unit    (str): convert to this data unit. Example:
                          (bps, Kbps, Mbps, Gbps... KB, KiB, MB, MiB...)

    Keyword arguments (opt):
        from_time  (str): Specify the time frame used in from_unit
                          (seconds, minutes, hours, days, months)
                          default: seconds
        to_time    (str): Specify the time frame used in to_unit
                          (seconds, minutes, hours, days, months)
                          default: seconds

    bps, Kbps, Mbps, Gbps... = decimal base = 1000^n
    KB, MB, GB, TB...        = decimal base = 1000^n
    KiB, MiB, GiB, TiB...    = binary base  = 1024^n

    References:
        - https://en.wikipedia.org/wiki/Units_of_information
        - https://physics.nist.gov/cuu/Units/binary.html

    Returns: tuple
       (number_converted, to_unit/to_time)

    Example:
    >>> bandwidth_converter(100, from_unit="Mbps", to_unit="MB")
    (12.5, 'MB/seconds')
    >>> bandwidth_converter(100, from_unit="Mbps", to_unit="GB", to_time="hours")
    (45.0, 'GB/hours')
    >>> bandwidth_converter(1, from_unit="Gbps", to_unit="MB")
    (125.0, 'MB/seconds')
    >>> bandwidth_converter(10, from_unit="Gbps", to_unit="GB")
    (1.25, 'GB/seconds')
    >>> bandwidth_converter(10, from_unit="Gbps", to_unit="TB", to_time="hours")
    (4.5, 'TB/hours')
    >>> bandwidth_converter(10, from_unit="GB", to_unit="Gbps")
    (80.0, 'Gbps/seconds')
    >>> Convert 2.25 GB per hours to Mbps # doctest: +SKIP
    >>> bandwidth_converter(2.25, from_unit="GB", from_time="hours", to_unit="Mbps", to_time="seconds") # noqa
    (5.0, 'Mbps/seconds')
    """
    unit_power = {
        "bps": 1,
        "Kbps": 1000,
        "Mbps": 1000 ** 2,
        "Gbps": 1000 ** 3,
        "Tbps": 1000 ** 4,
        "Pbps": 1000 ** 5,
        "Ebps": 1000 ** 6,
        "Bytes": 1,
        "KB": 1000,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3,
        "TB": 1000 ** 4,
        "PB": 1000 ** 5,
        "EB": 1000 ** 6,
        "KiB": 1024,
        "MiB": 1024 ** 2,
        "GiB": 1024 ** 3,
        "TiB": 1024 ** 4,
        "PiB": 1024 ** 5,
        "EiB": 1024 ** 6,
    }

    time_in_sec = {
        "seconds": 1,
        "minutes": 60,
        "hours": 3600,
        "days": 3600 * 24,
        "months": 3600 * 24 * 30,
    }

    if from_unit not in unit_power or to_unit not in unit_power:
        raise ValueError(
            "invalid unit. It must be {}".format(", ".join(unit_power.keys()))
        )

    if from_time not in time_in_sec or to_time not in time_in_sec:
        raise ValueError(
            "invalid time. It must be {}".format(", ".join(time_in_sec.keys()))
        )

    # Convert input number to bps
    bps = (float(number) * int(unit_power[from_unit])) / time_in_sec[from_time]
    if not from_unit.endswith("bps"):
        bps = bps * 8

    # to_unit is bits or bytes
    new_unit = bps if to_unit.endswith("bps") else bps / 8
    # Convert to new unit
    new_unit = (new_unit / unit_power[to_unit]) * time_in_sec[to_time]

    return new_unit, "{}/{}".format(to_unit, to_time)


# vim: ts=4
