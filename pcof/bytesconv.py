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

    Exemple:
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


# vim: ts=4
