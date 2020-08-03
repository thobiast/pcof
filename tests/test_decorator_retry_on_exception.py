# -*- coding: utf-8 -*-
"""Test decorator retry_on_exception."""

import pytest
import logging
from pcof import decorators


def myfunc(*args, **kwargs):
    return "{}; {}".format(args, kwargs)


def my_func_raise(num, exception=None):
    if num < 0:
        raise (exception)
    else:
        return num


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
def test_retry_on_exception_return(args, kwargs, result):
    """
    Test decorator does not change function behavior
    """
    decorated_func = decorators.retry_on_exception()(myfunc)
    assert decorated_func(*args, **kwargs) == result


def test_retry_on_exception_no_options():
    """
    Test decorator without options

    @decorators.retry_on_exception.
    def myfunc():
        ...
    """
    decorated_func = decorators.retry_on_exception(myfunc)
    assert decorated_func() == "(); {}"


@pytest.mark.parametrize(
    "exception", [(TimeoutError), (KeyError), (FileExistsError), (FileNotFoundError)]
)
def test_retry_on_exception_excetion(exception):
    """
    Test if decorator raises the same exception function raises
    """
    with pytest.raises(exception):
        decorated_func = decorators.retry_on_exception(sleep_retry=0)(my_func_raise)
        decorated_func(-1, exception)


class MaxRetryReached(Exception):
    pass


@pytest.mark.parametrize(
    "exception", [(TimeoutError), (KeyError), (FileExistsError), (FileNotFoundError)]
)
def test_retry_on_exception_exception_error(exception):
    """
    Test if decorator raises custom exception
    """
    with pytest.raises(MaxRetryReached):
        decorated_func = decorators.retry_on_exception(
            exception_error=MaxRetryReached, sleep_retry=0
        )(my_func_raise)
        decorated_func(-1, exception)


@pytest.mark.parametrize("max_retry", [(1), (2), (3), (10), (20)])
def test_retry_on_exception_max_retry_reach(caplog, max_retry):
    """
    Test decorator max retries reach
    """
    caplog.set_level(logging.DEBUG)
    with pytest.raises(TimeoutError):
        decorated_func = decorators.retry_on_exception(
            exception_error=TimeoutError, sleep_retry=0, max_retry=max_retry
        )(my_func_raise)
        decorated_func(-1, TimeoutError)
    for record in caplog.records:
        assert "max retry '{}' reached. Giving up".format(max_retry) in caplog.text


@pytest.mark.parametrize(
    "loglevel", [("DEBUG"), ("INFO"), ("WARNING"), ("ERROR"), ("CRITICAL")]
)
def test_retry_on_exception_parameters_log(caplog, loglevel):
    caplog.set_level(logging.DEBUG)
    decorated_func = decorators.retry_on_exception(loglevel=loglevel)(myfunc)
    decorated_func()
    for record in caplog.records:
        assert record.levelname == loglevel
        assert "Decorator retry for function: " in caplog.text


# vim: ts=4
