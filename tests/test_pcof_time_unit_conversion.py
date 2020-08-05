# -*- coding: utf-8 -*-
"""Test time_unit_conversion function."""

import pytest
from pcof import pcof


@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (60, "seconds", "seconds", "60"),
        (60, "seconds", "minutes", "1"),
        (3600, "seconds", "hours", "1"),
        (28800, "seconds", "hours", "8"),
        (86400, "seconds", "days", "1"),
        (604800, "seconds", "days", "7"),
        (604800, "seconds", "weeks", "1"),
        (2592000, "seconds", "months", "1"),
        (31536000, "seconds", "years", "1"),
    ],
)
def test_time_unit_conversion_from_sec(num, from_unit, to_unit, result):
    """Test conversion from seconds."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "minutes", "seconds", "60"),
        (1, "minutes", "minutes", "1"),
        (60, "minutes", "hours", "1"),
        (300, "minutes", "hours", "5"),
        (1440, "minutes", "days", "1"),
        (10080, "minutes", "days", "7"),
        (10080, "minutes", "weeks", "1"),
        (43200, "minutes", "months", "1"),
        (525600, "minutes", "years", "1"),
    ],
)
def test_time_unit_conversion_from_min(num, from_unit, to_unit, result):
    """Test conversion from minutes."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "hours", "seconds", "3600"),
        (1, "hours", "minutes", "60"),
        (24, "hours", "minutes", "1440"),
        (1, "hours", "hours", "1"),
        (24, "hours", "days", "1"),
        (168, "hours", "days", "7"),
        (216, "hours", "days", "9"),
        (168, "hours", "weeks", "1"),
        (840, "hours", "weeks", "5"),
        (720, "hours", "months", "1"),
        (8760, "hours", "years", "1"),
    ],
)
def test_time_unit_conversion_from_hours(num, from_unit, to_unit, result):
    """Test conversion from hours."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "days", "seconds", "86400"),
        (1, "days", "minutes", "1440"),
        (4, "days", "minutes", "5760"),
        (1, "days", "hours", "24"),
        (2, "days", "hours", "48"),
        (1, "days", "days", "1"),
        (7, "days", "weeks", "1"),
        (28, "days", "weeks", "4"),
        (30, "days", "months", "1"),
        (90, "days", "months", "3"),
        (365, "days", "years", "1"),
    ],
)
def test_time_unit_conversion_from_days(num, from_unit, to_unit, result):
    """Test conversion from days."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "weeks", "seconds", "604800"),
        (1, "weeks", "minutes", "10080"),
        (2, "weeks", "minutes", "20160"),
        (1, "weeks", "hours", "168"),
        (3, "weeks", "hours", "504"),
        (1, "weeks", "days", "7"),
        (2, "weeks", "days", "14"),
        (1, "weeks", "weeks", "1"),
    ],
)
def test_time_unit_conversion_from_weeks(num, from_unit, to_unit, result):
    """Test conversion from weeks."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "months", "seconds", "2592000"),
        (1, "months", "minutes", "43200"),
        (4, "months", "minutes", "172800"),
        (1, "months", "hours", "720"),
        (1, "months", "days", "30"),
        (1, "months", "months", "1"),
        (12, "months", "years", "1"),
    ],
)
def test_time_unit_conversion_from_months(num, from_unit, to_unit, result):
    """Test conversion from months."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, result",
    [
        (1, "years", "seconds", "31536000"),
        (1, "years", "minutes", "525600"),
        (1, "years", "hours", "8760"),
        (1, "years", "days", "365"),
        (1, "years", "weeks", "52"),
        (1, "years", "months", "12"),
        (2, "years", "months", "24"),
        (1, "years", "years", "1"),
    ],
)
def test_time_unit_conversion_from_years(num, from_unit, to_unit, result):
    """Test conversion from years."""
    assert (
        pcof.time_unit_conversion(num, from_unit=from_unit, to_unit=to_unit) == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, prec, result",
    [
        (1, "years", "weeks", 4, "52.1429"),
        (36, "hours", "days", 1, "1.5"),
        (10, "days", "weeks", 4, "1.4286"),
        (10, "days", "months", 2, "0.33"),
    ],
)
def test_time_unit_conversion_precision(num, from_unit, to_unit, prec, result):
    """Test precision conversion."""
    assert (
        pcof.time_unit_conversion(
            num, from_unit=from_unit, to_unit=to_unit, precision=prec
        )
        == result
    )


#################################
@pytest.mark.parametrize(
    "num, from_unit, to_unit, d_month, result",
    [
        (1, "months", "days", 30.4167, "30.4167"),
        (3, "months", "days", 30.4167, "91.2501"),
        (1, "months", "hours", 30.4167, "730.0008"),
    ],
)
def test_time_unit_conversion_custom_month(num, from_unit, to_unit, d_month, result):
    """Test conversion with custom day month."""
    assert (
        pcof.time_unit_conversion(
            num, from_unit=from_unit, to_unit=to_unit, precision=4, days_month=d_month,
        )
        == result
    )


#################################
def test_time_unit_conversion_raise():
    """Test exceptions."""
    with pytest.raises(ValueError, match=r"Invalid unit. It must be.*"):
        pcof.time_unit_conversion(1, from_unit="xxxxx", to_unit="hours")

    with pytest.raises(ValueError, match=r"Invalid unit. It must be.*"):
        pcof.time_unit_conversion(1, from_unit="hours", to_unit="xxxx")

    with pytest.raises(ValueError, match=r"Invalid unit. It must be.*"):
        pcof.time_unit_conversion(1, from_unit="xxx", to_unit="xxxx")

    with pytest.raises(TypeError, match="number must be int"):
        pcof.time_unit_conversion("x", from_unit="hours", to_unit="hours")


# vim: ts=4
