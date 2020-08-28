# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Percentage Calculator
"""


def y_what_pct_of_x(number1, number2, *, precision="2"):  # pragma: no cover
    """
    Calculate the percentage of number1 to number2.

    Number1 is what percent of number2.

    Arguments:
        number1     (int): number
        number2     (int): number

    Keyword arguments (opt):
        precision   (int): number of digits after the decimal point
                           default is 2

    Returns:
        (str):  Pct value

    Example:
    >>> y_what_pct_of_x(30, 90)    # 30 is what percent of 90?
    '33.33%'
    >>> y_what_pct_of_x(30, 90, precision=0)
    '33%'
    >>> y_what_pct_of_x(30, 90, precision=4)
    '33.3333%'
    >>> y_what_pct_of_x(10, 50, precision=0) # 10 is what percent of 50?
    '20%'
    """
    try:
        num_pct = (number1 / number2) * 100
        return "{0:.{prec}f}%".format(num_pct, prec=precision)
    except ZeroDivisionError:
        return "{0:.{prec}f}%".format(0, prec=precision)


def x_pct_of_number(pct, number, *, precision="2"):  # pragma: no cover
    """
    Calculate what is the x% of a number.

    Arguments:
        pct        (int): percentage
        number     (int): number

    Keyword arguments (opt):
        precision  (int): number of digits after the decimal point
                          default is 2

    Returns:
        (str):  number

    Example:
    >>> x_pct_of_number(33.333, 90)     # what is 33.333% of 90?
    '30.00'
    >>> x_pct_of_number(40, 200)        # what is 40% of 200?
    '80.00'
    >>> x_pct_of_number(40.9, 200)      # what is 40.9% of 200?
    '81.80'
    >>> x_pct_of_number(40.9, 200, precision=4)
    '81.8000'
    >>> x_pct_of_number(40.9, 200, precision=0)
    '82'
    """
    num = number * pct / 100
    return "{0:.{prec}f}".format(num, prec=precision)


def pct_change_from_x_to_y(number1, number2, *, precision="2"):  # pragma: no cover
    """
    Calculate percent increase/decrease from number1 to number2.

    Arguments:
        number1    (int): start value (from)
        number2    (int): end value (to)

    Keyword arguments (opt):
        precision  (int): number of digits after the decimal point
                          default is 2

    Returns:
        (str):  number

    Example:
    >>> pct_change_from_x_to_y(100, 110)  # what is the pct increase from 100 to 110?
    '10.00%'
    >>> pct_change_from_x_to_y(100, 90)   # what is the pct from 100 to 90?
    '-10.00%'
    >>> pct_change_from_x_to_y(25, 50, precision=0)
    '100%'
    """
    try:
        num_pct = ((number2 - number1) / number1) * 100
        return "{0:.{prec}f}%".format(num_pct, prec=precision)
    except ZeroDivisionError:
        return "{0:.{prec}f}%".format(0, prec=precision)


# vim: ts=4
