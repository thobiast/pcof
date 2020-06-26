# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

pcof Decorators
"""

# Author: Thobias Salazar Trevisan
# Site: http://thobias.org

import functools
import logging
import time


LOG = logging.getLogger(__name__)


def num_calls(_func=None, *, loglevel="DEBUG", print_info=False):
    """
    Count the number of times a function is called.

    Decorator keyword arguments (optional):
        loglevel          (str):  log level used to show the number of
                                  calls information. (default DEBUG)
        print_info (True/False):  print function number of call information
                                  (default False)

    Example:
    @num_calls
    def my_func():
        print("my func")

    @num_calls(print_info=True)
    def my_other_func():
        print("my other func")
    """
    def decorator_num_calls(func):
        @functools.wraps(func)
        def wrapped_f(*args, **kwargs):
            wrapped_f.numcalls += 1

            output = "Decorator num_calls: {} called {} times".format(
                        func.__name__, wrapped_f.numcalls)

            getattr(LOG, loglevel.lower())(output)
            if print_info:
                print(output)

            return func(*args, **kwargs)

        wrapped_f.numcalls = 0
        return wrapped_f

    # wrapper to decorator, so it can be used with and without parameter
    if _func is None:
        return decorator_num_calls
    else:
        return decorator_num_calls(_func)


def time_elapsed(_func=None, *, loglevel="DEBUG", print_info=False):
    """
    Calculate elapsed time in seconds.

    Decorator keyword arguments (optional):
        loglevel          (str):  log level used to show elapsed time
                                  (default DEBUG)
        print_info (True/False):  print elapsed time (default False)

    Example:
    @time_elapsed
    def my_func():
        print("my func")

    @time_elapsed(print_info=True)
    def my_other_func():
        print("my other func")
    """
    def decorator_time_elapsed(func):
        @functools.wraps(func)
        def wrapped_f(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            # keep track of total elapsed time for all execution of the function
            wrapped_f.elapsed += elapsed_time

            output = "Decorator time_elapsed: {} args: {} kwargs: {} - " \
                     "elapsed time {:.4f} seconds. " \
                     "This function all execution elapsed time: {:.4f} " \
                     "seconds".format(
                         func.__name__, args, kwargs,
                         elapsed_time, wrapped_f.elapsed)

            getattr(LOG, loglevel.lower())(output)
            if print_info:
                print(output)

            return result

        wrapped_f.elapsed = 0
        return wrapped_f

    # wrapper to decorator, so it can be used with and without parameter
    if _func is None:
        return decorator_time_elapsed
    else:
        return decorator_time_elapsed(_func)

# vim: ts=4
