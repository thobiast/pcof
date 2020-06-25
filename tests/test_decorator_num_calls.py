# -*- coding: utf-8 -*-
"""Test decorator num_calls."""

import pytest
from pcof import decorators


def myfunc(*args, **kwargs):
    return '{}; {}'.format(args, kwargs)


def myfunc_two(*args, **kwargs):
    return '{}; {}'.format(args, kwargs)


@pytest.mark.parametrize("args, kwargs, result", [
    ([], {}, "(); {}"),
    ([1], {}, "(1,); {}"),
    ([1, 2], {}, "(1, 2); {}"),
    ([], {'opt1': 'test'}, "(); {'opt1': 'test'}"),
    ([], {'opt1': 1, 'opt2': True}, "(); {'opt1': 1, 'opt2': True}"),
    ([1, 2], {'opt1': 1, 'opt2': True}, "(1, 2); {'opt1': 1, 'opt2': True}"),
])
def test_num_calls_return(args, kwargs, result):
    """
    Test decorator does not change function behavior
    """
    decorated_func = decorators.num_calls()(myfunc)
    assert decorated_func(*args, **kwargs) == result


def test_num_calls():
    """
    Check decorator information
    """
    decorated_func = decorators.num_calls()(myfunc)

    assert decorated_func.numcalls == 0
    decorated_func()
    assert decorated_func.numcalls == 1
    decorated_func()
    assert decorated_func.numcalls == 2
    decorated_func()
    assert decorated_func.numcalls == 3
    decorated_func()
    assert decorated_func.numcalls == 4


def test_num_calls_share():
    """
    Check decorator does not share num_calls between decorator
    """
    decorated_func = decorators.num_calls()(myfunc)
    decorated_func_two = decorators.num_calls()(myfunc_two)

    assert decorated_func.numcalls == 0
    assert decorated_func_two.numcalls == 0

    decorated_func()
    assert decorated_func.numcalls == 1
    assert decorated_func_two.numcalls == 0

    decorated_func()
    assert decorated_func.numcalls == 2
    assert decorated_func_two.numcalls == 0

    decorated_func_two()
    assert decorated_func.numcalls == 2
    assert decorated_func_two.numcalls == 1

    decorated_func_two()
    assert decorated_func.numcalls == 2
    assert decorated_func_two.numcalls == 2

    decorated_func()
    assert decorated_func.numcalls == 3
    assert decorated_func_two.numcalls == 2


def test_num_calls_no_options():
    """
    Test decorator without options

    @decorators.num_calls
    def myfunc():
        ...
    """
    decorated_func = decorators.num_calls(myfunc)
    assert decorated_func() == "(); {}"
    assert decorated_func.numcalls == 1


def test_num_calls_parameters(capsys):
    decorated_func = decorators.num_calls(print_info=True)(myfunc)
    decorated_func()
    out, err = capsys.readouterr()
    assert "myfunc called 1 times" in out
    decorated_func()
    out, err = capsys.readouterr()
    assert "myfunc called 2 times" in out

# vim: ts=4
