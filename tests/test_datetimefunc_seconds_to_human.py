# -*- coding: utf-8 -*-
"""Test seconds_to_human function."""

import pytest
from pcof import datetimefunc


@pytest.mark.parametrize(
    "seconds, result",
    [
        (1, "1 Seconds"),
        (60, "1 Minutes"),
        (300, "5 Minutes"),
        (310, "5 Minutes, 10 Seconds"),
        (180972, "2 Days, 2 Hours, 16 Minutes, 12 Seconds"),
        (5191572, "2 Months, 2 Hours, 6 Minutes, 12 Seconds"),
        (238373792, "7 Years, 6 Months, 23 Days, 22 Hours, 56 Minutes, 32 Seconds"),
    ],
)
def test_seconds_to_human(seconds, result):
    assert datetimefunc.seconds_to_human(seconds) == result


def test_seconds_to_human_zero():
    assert datetimefunc.seconds_to_human(0) == "0 Seconds"


@pytest.mark.parametrize(
    "seconds, unit, result",
    [
        (10810, "Minutes", "180 Minutes, 10 Seconds"),
        (980810, "Minutes", "16346 Minutes, 50 Seconds"),
        (51919157, "Days", "600 Days, 21 Hours, 59 Minutes, 17 Seconds"),
    ],
)
def test_seconds_to_human_unit(seconds, unit, result):
    assert datetimefunc.seconds_to_human(seconds, unit=unit) == result


def test_seconds_to_human():
    with pytest.raises(
        TypeError, match="error: seconds_to_human: seconds must be greater than 0"
    ):
        datetimefunc.seconds_to_human(-10)
    with pytest.raises(TypeError, match="error: seconds_to_human: unit is invalid"):
        datetimefunc.seconds_to_human(10, unit="invalid")
    with pytest.raises(TypeError, match="seconds must be int"):
        datetimefunc.seconds_to_human("10")


# vim: ts=4
