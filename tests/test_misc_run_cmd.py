# -*- coding: utf-8 -*-
"""Test run_cmd function."""

import pytest
from pcof import misc


def test_run_cmd():
    assert misc.run_cmd("echo test") == (0, "test\n")
    assert misc.run_cmd("ls > /dev/null") == (0, "")
    assert misc.run_cmd("cmd_not_found test")[0] == 127


# vim: ts=4
