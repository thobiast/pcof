# -*- coding: utf-8 -*-
"""Test convert_datetime_to_tz function."""

import datetime
import pytest
from pcof import pcof


def test_convert_datetime_to_tz():
    # from utc
    assert str(pcof.convert_datetime_to_tz(
            date='2019-04-26T10:38:05Z',
            date_fmt="%Y-%m-%dT%H:%M:%SZ",
            from_tz='UTC',
            to_tz='America/Sao_Paulo')) == "2019-04-26 07:38:05-03:00"
    # from America/Sao_Paulo to default America/Sao_Paulo
    # so it actually does not convert
    assert str(pcof.convert_datetime_to_tz(
            date='2019-04-26T10:38:05Z',
            date_fmt="%Y-%m-%dT%H:%M:%SZ",
            from_tz='America/Sao_Paulo')) == "2019-04-26 10:38:05-03:00"
    # convert from America/Sao_Paulo to New York
    # difference one hour
    assert str(pcof.convert_datetime_to_tz(
            date='2019-04-26T10:38:05Z',
            date_fmt="%Y-%m-%dT%H:%M:%SZ",
            from_tz='America/Sao_Paulo',
            to_tz="America/New_York")) == "2019-04-26 09:38:05-04:00"
    assert isinstance(pcof.convert_datetime_to_tz(
            date='2019-04-26T10:38:05Z',
            date_fmt="%Y-%m-%dT%H:%M:%SZ",
            from_tz='UTC',
            to_tz='America/Sao_Paulo'), datetime.datetime)

# vim: ts=4
