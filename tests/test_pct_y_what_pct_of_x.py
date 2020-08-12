# -*- coding: utf-8 -*-
"""Test y_what_pct_of_x function."""

import pytest
from pcof import pct


def test_y_what_pct_of_x():
    assert pct.y_what_pct_of_x(10, 100) == "10.00%"
    assert pct.y_what_pct_of_x(10, 50) == "20.00%"
    assert pct.y_what_pct_of_x(10, 50, precision=0) == "20%"


# vim: ts=4
