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
                func.__name__, wrapped_f.numcalls
            )

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

            output = (
                "Decorator time_elapsed: {} args: {} kwargs: {} - "
                "elapsed time {:.4f} seconds. "
                "This function all execution elapsed time: {:.4f} "
                "seconds".format(
                    func.__name__, args, kwargs, elapsed_time, wrapped_f.elapsed
                )
            )

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


def debug(_func=None, *, loglevel="DEBUG", print_info=False):
    """
    Show function parameters and return values.

    Decorator keyword arguments (optional):
        loglevel          (str):  log level used to show debug information.
                                  (default DEBUG)
        print_info (True/False):  print debug information.
                                  (default False)

    Example:
    @debug
    def my_func():
        print("my func")
        return True

    @debug(print_info=True)
    def my_other_func(my_param):
        print("my other func")
    """

    def decorator_debug(func):
        @functools.wraps(func)
        def wrapped_f(*args, **kwargs):
            func_call = (
                "Decorator debug: "
                "Calling function: {} arguments: args: {}; kwargs: {}".format(
                    func.__name__, args, kwargs
                )
            )

            getattr(LOG, loglevel.lower())(func_call)
            if print_info:
                print(func_call)

            result = func(*args, **kwargs)

            func_return = "Decorator debug: function: {} returns: {}".format(
                func.__name__, result
            )
            getattr(LOG, loglevel.lower())(func_return)
            if print_info:
                print(func_return)

            return result

        return wrapped_f

    # wrapper to decorator, so it can be used with and without parameter
    if _func is None:
        return decorator_debug
    else:
        return decorator_debug(_func)


def retry_on_exception(
    _func=None,
    *,
    exception=(Exception,),
    loglevel="DEBUG",
    max_retry=5,
    sleep_retry=1,
    exception_error=None
):
    """
    Retry function execution if exception raises.

    Decorator keyword arguments (optional):
        exception            (tuple): Tuple with exceptions that decorator will retry
                                      function's execution
                                      (default any exception)
        loglevel               (str): Log level used to show debug information.
                                      (default DEBUG)
        max_retry              (int): Max number of retries. -1 to retry forever
                                      (default 5)
        sleep_retry            (int): Time in seconds to wait between retries
                                      (default 1)
        exception_error  (exception): Exception that decorator will raise if
                                      max_retry is reached without success
                                      (default the same exception function raises)

    Example:
    # Retry function if any exception raise
    @retry_on_exception
    def my_func():
        print("my func")
        raise (TimeoutError)

    # Retry only with exceptions: TimeoutErrorr, IndexError and Retry max of 10 times
    @retry_on_exception(exception=(TimeoutError, IndexError), max_retry=10)
    def my_other_func(my_param):
        print("my other func")
    """

    def decorator_retry(func):
        @functools.wraps(func)
        def wrapped_f(*args, **kwargs):
            current_retry = 1
            log_prefix = "Decorator retry for function: {} -".format(func.__name__)

            while True:
                log_msg = "{} retry: {} of {}".format(
                    log_prefix, current_retry, max_retry
                )
                getattr(LOG, loglevel.lower())(log_msg)

                try:
                    return func(*args, **kwargs)
                except exception as error:
                    log_msg = "{} exception catched: {}".format(log_prefix, repr(error))
                    getattr(LOG, loglevel.lower())(log_msg)

                    if max_retry != -1:
                        current_retry += 1
                        if current_retry > max_retry:
                            log_msg = "{} max retry '{}' reached. Giving up".format(
                                log_prefix, max_retry
                            )
                            getattr(LOG, loglevel.lower())(log_msg)
                            if exception_error:
                                raise exception_error("max retry reached")
                            else:
                                raise

                    log_msg = "{} waiting: {}s for next retry".format(
                        log_prefix, sleep_retry
                    )
                    getattr(LOG, loglevel.lower())(log_msg)
                    time.sleep(sleep_retry)

        return wrapped_f

    # wrapper to decorator, so it can be used with and without parameter
    if _func is None:
        return decorator_retry
    else:
        return decorator_retry(_func)


# vim: ts=4
