# -*- coding: utf-8 -*-
"""Test decorator time_elapsed."""

import pytest
import time
from pcof import decorators


def myfunc(*args, **kwargs):
    return '{}; {}'.format(args, kwargs)


def myfunc_two(*args, **kwargs):
    time.sleep(0.1)
    return '{}; {}'.format(args, kwargs)


@pytest.mark.parametrize("args, kwargs, result", [
    ([], {}, "(); {}"),
    ([1], {}, "(1,); {}"),
    ([1, 2], {}, "(1, 2); {}"),
    ([], {'opt1': 'test'}, "(); {'opt1': 'test'}"),
    ([], {'opt1': 1, 'opt2': True}, "(); {'opt1': 1, 'opt2': True}"),
    ([1, 2], {'opt1': 1, 'opt2': True}, "(1, 2); {'opt1': 1, 'opt2': True}"),
])
def test_time_elapsed_return(args, kwargs, result):
    """
    Test decorator does not change function behavior
    """
    decorated_func = decorators.time_elapsed()(myfunc)
    assert decorated_func(*args, **kwargs) == result


def test_time_elapsed_total():
    """
    Check decorator information
    """
    decorated_func_two = decorators.time_elapsed()(myfunc_two)

    total = decorated_func_two.elapsed
    assert total == 0

    decorated_func_two()
    total += decorated_func_two.elapsed
    assert total == decorated_func_two.elapsed

    decorated_func_two()
    total += decorated_func_two.elapsed
    assert total > decorated_func_two.elapsed


def test_time_elapsed_share():
    """
    Check decorator does not share time_elapsed between decorator
    """
    decorated_func = decorators.time_elapsed()(myfunc)
    decorated_func_two = decorators.time_elapsed()(myfunc_two)

    assert decorated_func.elapsed == 0
    assert decorated_func_two.elapsed == 0

    decorated_func()
    assert decorated_func.elapsed > 0
    assert decorated_func_two.elapsed == 0

    decorated_func()
    assert decorated_func.elapsed > 0
    assert decorated_func_two.elapsed == 0

    decorated_func_two()
    assert decorated_func.elapsed > 0
    assert decorated_func_two.elapsed > 0


def test_time_elapsed_no_options():
    """
    Test decorator without options

    @decorators.time_elapsed
    def myfunc():
        ...
    """
    decorated_func = decorators.time_elapsed(myfunc)
    assert decorated_func() == "(); {}"
    assert decorated_func.elapsed > 0


def test_time_elapsed_parameters(capsys):
    decorated_func = decorators.time_elapsed(print_info=True)(myfunc)
    decorated_func()
    out, err = capsys.readouterr()
    assert "Decorator time_elapsed: myfunc args: () kwargs: {} - elapsed time" in out
    assert "seconds\n" in out

# vim: ts=4
