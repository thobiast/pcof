# -*- coding: utf-8 -*-
"""Test epoch_time functions."""

import pytest
from pcof import pcof


##############################################################################
# epoch_time_to_human
##############################################################################
def test_epoch_time_to_human():
    assert pcof.epoch_time_to_human(
            1530324373,
            date_format='%m/%d/%Y %H:%M:%S',
            utc='yes') == "06/30/2018 02:06:13"
    assert pcof.epoch_time_to_human(
            1590760671, date_format='%m/%Y') == "05/2020"
    assert isinstance(pcof.epoch_time_to_human(1530324373), str)

def test_epoch_time_to_human_raise():
    with pytest.raises(TypeError, match="epoch time must be int"):
        pcof.epoch_time_to_human("1283820")


##############################################################################
# epoch_time_now
##############################################################################
def test_epoch_time_now():
    assert isinstance(pcof.epoch_time_now(), int)
    assert isinstance(pcof.epoch_time_now(utc="yes"), int)

def test_epoch_time_now_raise():
    with pytest.raises(ValueError, match="error: epoch_time_now: utc is invalid"):
        pcof.epoch_time_now(utc="XX")


##############################################################################
# epoch_time_min_ago
##############################################################################
def test_epoch_time_min_ago():
    assert isinstance(pcof.epoch_time_min_ago(), int)
    assert isinstance(pcof.epoch_time_min_ago(minutes=30), int)
    assert isinstance(pcof.epoch_time_min_ago(minutes=10, utc="yes"), int)

def test_epoch_time_min_raise():
    with pytest.raises(TypeError, match="minutes must be int"):
        pcof.epoch_time_min_ago("10")


##############################################################################
# epoch_time_hours_ago
##############################################################################
def test_epoch_time_hours_ago():
    assert isinstance(pcof.epoch_time_hours_ago(), int)
    assert isinstance(pcof.epoch_time_hours_ago(hours=10), int)
    assert isinstance(pcof.epoch_time_hours_ago(hours=10, utc="yes"), int)

def test_epoch_time_hours_raise():
    with pytest.raises(TypeError, match="hours must be int"):
        pcof.epoch_time_hours_ago("10")

##############################################################################
# epoch_time_days_ago
##############################################################################
def test_epoch_time_days_ago():
    assert isinstance(pcof.epoch_time_days_ago(), int)
    assert isinstance(pcof.epoch_time_days_ago(days=7), int)
    assert isinstance(pcof.epoch_time_days_ago(days=10, utc="yes"), int)

def test_epoch_time_days_raise():
    with pytest.raises(TypeError, match="days must be int"):
        pcof.epoch_time_days_ago("10")

# vim: ts=4
