# -*- coding: utf-8 -*-
"""Test run_cmd function."""

import pytest
from pcof import pcof


def test_run_cmd():
    assert pcof.run_cmd("echo test") == (0, "test\n")
    assert pcof.run_cmd("ls > /dev/null") == (0, "")
    assert pcof.run_cmd("cmd_not_found test")[0] == 127

# vim: ts=4
