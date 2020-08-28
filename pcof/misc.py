# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Miscellaneous functions
"""


import collections
import hashlib
import logging
import smtplib
import subprocess
import sys


##############################################################################
##############################################################################
# Print text
##############################################################################
##############################################################################


def msg(color, msg_text, exitcode=0, *, end="\n", flush=True, output=None):
    """
    Print colored text.

    Arguments:
        color          (str): color name (blue, red, green, yellow,
                              cyan or nocolor)
        msg_text       (str): text to be printed
        exitcode  (int, opt): Optional parameter. If exitcode is different
                              from zero, it terminates the script, i.e,
                              it calls sys.exit with the exitcode informed

    Keyword arguments (optional):
        end            (str): string appended after the last char in "msg_text"
                              default a newline
        flush   (True/False): whether to forcibly flush the stream.
                              default True
        output      (stream): a file-like object (stream).
                              default sys.stdout

    Example:
        msg("blue", "nice text in blue")
        msg("red", "Error in my script. terminating", 1)
    """
    color_dic = {
        "blue": "\033[0;34m",
        "red": "\033[1;31m",
        "green": "\033[0;32m",
        "yellow": "\033[0;33m",
        "cyan": "\033[0;36m",
        "resetcolor": "\033[0m",
    }

    if not output:
        output = sys.stdout

    if not color or color == "nocolor":
        print(msg_text, end=end, file=output, flush=flush)
    else:
        if color not in color_dic:
            raise ValueError("Invalid color")
        print(
            "{}{}{}".format(color_dic[color], msg_text, color_dic["resetcolor"]),
            end=end,
            file=output,
            flush=flush,
        )

    if exitcode:
        sys.exit(exitcode)


##############################################################################
##############################################################################
# Email
##############################################################################
##############################################################################


def send_email(
    mail_from, mail_to, subject, body, mailserver="localhost"
):  # pragma: no cover
    """
    Send an email using smtplib module.

    Arguments:
        mail_from        (str): send email from this address
        mail_to          (str): send email to this address
        subject          (str): mail subject
        mail_server (str, opt): mail server address. Default is localhost
    """
    mail_msg = """\
From: %s
To: %s
Subject: %s

%s
""" % (
        mail_from,
        mail_to,
        subject,
        body,
    )

    # send the email
    try:
        smtpobj = smtplib.SMTP(mailserver)
        smtpobj.sendmail(mail_from, mail_to, mail_msg)
    finally:
        smtpobj.quit()


##############################################################################
##############################################################################
# Log
##############################################################################
##############################################################################


def setup_logging(
    logfile=None, *, filemode="a", date_format=None, log_level="DEBUG"
):  # pragma: no cover
    """
    Configure logging.

    Arguments (opt):
        logfile     (str): log file to write the log messages
                               If not specified, it shows log messages
                               on screen (stderr)
    Keyword arguments (opt):
        filemode    (a/w): a - log messages are appended to the file (default)
                           w - log messages overwrite the file
        date_format (str): date format in strftime format
                           default is %m/%d/%Y %H:%M:%S
        log_level   (str): specifies the lowest-severity log message
                           DEBUG, INFO, WARNING, ERROR or CRITICAL
                           default is DEBUG
    """
    dict_level = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    if log_level not in dict_level:
        raise ValueError("Invalid log_level")
    if filemode not in ["a", "w"]:
        raise ValueError("Invalid filemode")

    if not date_format:
        date_format = "%m/%d/%Y %H:%M:%S"

    log_fmt = "%(asctime)s %(module)s %(funcName)s %(levelname)s %(message)s"

    logging.basicConfig(
        level=dict_level[log_level],
        format=log_fmt,
        datefmt=date_format,
        filemode=filemode,
        filename=logfile,
    )

    return logging.getLogger(__name__)


##############################################################################
##############################################################################
# Dictionary
##############################################################################
##############################################################################


def nested_dict():  # pragma: no cover
    """
    Return a nested dictionary (arbitrary number of levels).

    Example:
    >>> mydict = nested_dict()
    >>> mydict['a1']['b1']['c1'] = 'test_1'
    >>> mydict['a1']['b2'] = 'test_2'
    >>> mydict['a1']['b3'] = 'test_3'
    >>> mydict.keys()
    dict_keys(['a1'])
    >>> mydict['a1'].keys()
    dict_keys(['b1', 'b2', 'b3'])
    >>> mydict['a1']['b1'].keys()
    dict_keys(['c1'])
    >>> mydict['a1']['b1']['c1']
    'test_1'
    >>> mydict['a1']['b2']
    'test_2'
    >>> print(mydict) # doctest: +SKIP
    defaultdict(<function nested_dict at 0x7f0239f4aee0>,
        {'a1': defaultdict(<function nested_dict at 0x7f0239f4aee0>,
        {'b1': defaultdict(<function nested_dict at 0x7f0239f4aee0>,
            {'c1': 'test_1'}),
        'b2': 'test_2',
        'b3': 'test_3'})})
    """
    return collections.defaultdict(nested_dict)


def find_key(dict_obj, key):
    """
    Return a value for a key in a dictionary.

    Function to loop over a dictionary and search for an specific key
    It supports nested dictionary

    Arguments:
        dict_obj    (obj): A list or a dictionary
        key         (str): dictionary key

    Return:
        (list)           : a list with values that matches the key

    Example:
    >>> x = {"A1": "A", "B1": { "A2": "AA"} }
    >>> find_key(x, "A1")
    ['A']
    >>> find_key(x, "A2")
    ['AA']
    >>> find_key(x, "YY")
    []
    >>> x = {"A1": "A", "B1": { "A1": "AA"} }
    >>> find_key(x, "A1")
    ['A', 'AA']
    """
    # List to store values
    results = []

    # if dict_obj is a dictionary
    if isinstance(dict_obj, dict):
        for k, v in dict_obj.items():
            # if value is == key
            if k == key:
                results.append(v)
            else:
                # call function again, it can be a nested dict
                results.extend(find_key(v, key))
    # If dict_obj is a list
    elif isinstance(dict_obj, list):
        # for each item, call again the function, as maybe there are
        # dict inside the list
        for item in dict_obj:
            results.extend(find_key(item, key))

    return results


def return_dict_value(dictionary, keys, *, ignore_key_error=False):  # pragma: no cover
    """
    Return a value from a dictionary.

    Recursively iterate over a dictionary and return value
    for the key. Key must be a list. Each element of the list refers
    to the level of the dicionary

    It helps to reduce number of code lines when we need to perform may
    try: except: to catch KeyErrors

    Arguments:
       dictionary              (dict): Dictionary
       keys                    (list): List with key(s)
       ignore_key_error  (True/False): Ignore key not found errors:
                                         True  - return '' if key not found
                                         False - raise exception
                                       default: False

    Example:
    >>> mydic = { 'a': 'value_a',
    ...           'b': {
    ...                  'b1': 'value_b1',
    ...                  'b2': 'value_b2'
    ...                },
    ...           'c': {
    ...                  'c1': {
    ...                          'c11': 'value_c11',
    ...                          'c12': 'value_c12'
    ...                         }
    ...                },
    ...          }
    >>> return_dict_value(mydic, ['a'])
    'value_a'
    >>> return_dict_value(mydic, ['b'])
    {'b1': 'value_b1', 'b2': 'value_b2'}
    >>> return_dict_value(mydic, ['b', 'b1'])
    'value_b1'
    >>> return_dict_value(mydic, ['c', 'c1', 'c12'])
    'value_c12'
    >>> return_dict_value(mydic, ['c', 'c1', 'c13'])
    Traceback (most recent call last):
    ...
    KeyError: 'c13'
    >>> return_dict_value(mydic, ['c', 'c1', 'c13'], ignore_key_error=True)
    ''
    >>> return_dict_value(mydic, ['x'], ignore_key_error=True)
    ''
    """
    # Check if there is more than one key
    if len(keys) > 1:
        # More keys in the last, call function again
        try:
            return return_dict_value(dictionary[keys[0]], keys[1:])
        except (KeyError, TypeError):
            if ignore_key_error:
                return ""
            raise
    else:
        # It is the last key, try to return the dict value for the key
        try:
            return dictionary[keys[0]]
        except (KeyError, TypeError):
            if ignore_key_error:
                return ""
            raise


##############################################################################
##############################################################################
# Execute command
##############################################################################
##############################################################################


def run_cmd(cmd):
    r"""
    Execute a command on the operating system.

    Arguments:
        cmd    (str): the command to be executed

    Return:
        - If command complete with return code zero
        return: command_return_code, stdout

        - If command completes with return code different from zero
        return: command_return_code, stderr


    Example:
    >>> run_cmd("echo test")
    (0, 'test\n')
    >>> run_cmd("cmd_does_not_exist") # doctest:+ELLIPSIS
    (127, '...cmd_does_not_exist:...not found\n')
    """
    process = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    # Poll process for new output until finished
    stdout_output = ""
    while True:
        nextline = process.stdout.readline()
        if nextline == "" and process.poll() is not None:
            break
        # print lines to stdout
        # sys.stdout.write(nextline)
        # sys.stdout.flush()
        stdout_output += nextline

    stderr = process.communicate()[1]

    if process.returncode:
        return process.returncode, stderr

    return process.returncode, stdout_output


##############################################################################
##############################################################################
# hash
##############################################################################
##############################################################################


def checksum_file(filename, *, algorithm="sha256", block_size=1048576):
    """
    Return checksums (hash) of a file.

    Arguments:
        filename           (str): file to check hash

    Keyword arguments (opt):
        algorithm          (str): algorithm used to calculate hash.
                                  default: sha256
        block_size         (int): chunk size to read the file (bytes)

    return:
        hex-encoded string

    Example:
    >>> checksum_file("my_file") # doctest: +SKIP
    '179b8c9510b2f068b94286c86610c6fe633ca44b5e541837ae9461bbdace7191'
    >>> checksum_file("my_file", algorithm="md5") # doctest: +SKIP
    'bdc28791ea81bafa7601e98f68b692e5'
    """
    try:
        file_hash = getattr(hashlib, algorithm)()
    except AttributeError:
        raise TypeError("hash algorithm not supported")

    if not isinstance(block_size, int):
        raise TypeError("block_size should be int")

    with open(filename, "rb") as fd:
        block = fd.read(block_size)
        while block:
            file_hash.update(block)
            block = fd.read(block_size)

    return file_hash.hexdigest()


# vim: ts=4
