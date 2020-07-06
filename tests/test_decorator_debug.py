# -*- coding: utf-8 -*-
"""Test decorator debug."""

import pytest
import logging
from pcof import decorators


def myfunc(*args, **kwargs):
    return "{}; {}".format(args, kwargs)


@pytest.mark.parametrize(
    "args, kwargs, result",
    [
        ([], {}, "(); {}"),
        ([1], {}, "(1,); {}"),
        ([1, 2], {}, "(1, 2); {}"),
        ([], {"opt1": "test"}, "(); {'opt1': 'test'}"),
        ([], {"opt1": 1, "opt2": True}, "(); {'opt1': 1, 'opt2': True}"),
        ([1, 2], {"opt1": 1, "opt2": True}, "(1, 2); {'opt1': 1, 'opt2': True}"),
    ],
)
def test_debug_return(args, kwargs, result):
    """
    Test decorator does not change function behavior
    """
    decorated_func = decorators.debug()(myfunc)
    assert decorated_func(*args, **kwargs) == result


def test_debug_no_options():
    """
    Test decorator without options

    @decorators.debug
    def myfunc():
        ...
    """
    decorated_func = decorators.debug(myfunc)
    assert decorated_func() == "(); {}"


def test_debug_parameters_print(capsys):
    decorated_func = decorators.debug(print_info=True)(myfunc)
    decorated_func()
    out, err = capsys.readouterr()
    assert (
        "Decorator debug: Calling function: myfunc arguments: args: (); kwargs: {}"
        == out.split("\n")[0]
    )
    assert "Decorator debug: function: myfunc returns: (); {}" == out.split("\n")[1]


def test_debug_parameters_print_false(capsys):
    decorated_func = decorators.debug(print_info=False)(myfunc)

    decorated_func()
    out, err = capsys.readouterr()
    assert "" == out


@pytest.mark.parametrize(
    "loglevel", [("DEBUG"), ("INFO"), ("WARNING"), ("ERROR"), ("CRITICAL")]
)
def test_debug_parameters_log(caplog, loglevel):
    caplog.set_level(logging.DEBUG)
    decorated_func = decorators.debug(loglevel=loglevel)(myfunc)
    decorated_func()
    for record in caplog.records:
        assert record.levelname == loglevel
        assert "Decorator debug: function: myfunc" in caplog.text


# vim: ts=4
