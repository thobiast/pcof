# -*- coding: utf-8 -*-
"""Test msg function."""

import pytest
from pcof import pcof


@pytest.mark.parametrize(
    "color, msg, result",
    [
        ("red", "test", "\033[1;31mtest\033[0m\n"),
        ("blue", "test", "\033[0;34mtest\033[0m\n"),
        ("yellow", "test", "\033[0;33mtest\033[0m\n"),
        ("", "test", "test\n"),
        ("nocolor", "test", "test\n"),
    ],
)
def test_msg(capsys, color, msg, result):
    """Test msg function."""
    pcof.msg(color, msg)
    out, err = capsys.readouterr()
    assert out == result


@pytest.mark.parametrize(
    "color, msg, end, result",
    [
        ("", "test", "", "test"),
        ("nocolor", "test", "--", "test--"),
        ("blue", "test", "", "\033[0;34mtest\033[0m"),
    ],
)
def test_msg_end(capsys, color, msg, end, result):
    """Test msg function."""
    pcof.msg(color, msg, end=end)
    out, err = capsys.readouterr()
    assert out == result


@pytest.mark.parametrize(
    "color, msg, retcode", [("red", "test", 8), ("", "test", 10), ("blue", "test", 2),]
)
def test_msg_exit(color, msg, retcode):
    """Test msg function exit code."""
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        pcof.msg(color, msg, retcode)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == retcode


def test_msg_error():
    with pytest.raises(ValueError, match="Invalid color"):
        pcof.msg("invalid_color", "test")


# vim: ts=4
