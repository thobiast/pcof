# -*- coding: utf-8 -*-
"""Test bytes2human function."""

import pytest
from pcof import pcof


def test_bytes2human():
    assert pcof.bytes2human(10) == ('10.00', 'Bytes')
    assert pcof.bytes2human("10") == ('10.00', 'Bytes')
    assert pcof.bytes2human("27273042329") == ('25.40', 'GB')
    assert pcof.bytes2human("27273042329", precision=1) == ('25.4', 'GB')
    assert pcof.bytes2human("27273042329", precision=1, unit="MB") == ('26009.6', 'MB')
    assert pcof.bytes2human("1099511627776") == ('1.00', 'TB')
    assert pcof.bytes2human("2251799813685248") == ('2.00', 'PB')


def test_bytes2human_raise():
    with pytest.raises(ValueError, match="value is not a number"):
        pcof.bytes2human("1x0")
    with pytest.raises(ValueError, match="base is not a number"):
        pcof.bytes2human("10", base="x")
    with pytest.raises(ValueError, match="precision is not a number"):
        pcof.bytes2human("10", precision="x")
    with pytest.raises(ValueError, match="value greater than the highest unit"):
        pcof.bytes2human(9999999999999999999999999)
    with pytest.raises(ValueError, match="unit must be KB, MB, GB, TB, PB, EB, ZB"):
        pcof.bytes2human("10", unit="GG")

# vim: ts=4
