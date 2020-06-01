# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

This module has a collection of many small generic useful functions.

Developed for Python 3
"""

# Author: Thobias Salazar Trevisan
# Site: http://thobias.org


import collections
import datetime
import logging
import smtplib
import subprocess
import sys

import prettytable

import pytz


##############################################################################
##############################################################################
# Print text
##############################################################################
##############################################################################

def msg(color, msg_text, exitcode=0, *, end='\n'):
    """
    Print colored text.

    Arguments:
        size           (str): color name (blue, red, green, yellow,
                              cyan or nocolor)

        msg_text       (str): text to be printed

        exitcode  (int, opt): Optional parameter. If exitcode is different
                              from zero, it terminates the script, i.e,
                              it calls sys.exit with the exitcode informed

    Keyword arguments (optional):
        end            (str): string appended after the last value,
                              default a newline

    Example:
        msg("blue", "nice text in blue")
        msg("red", "Error in my script. terminating", 1)
    """
    color_dic = {'blue': '\033[0;34m',
                 'red': '\033[1;31m',
                 'green': '\033[0;32m',
                 'yellow': '\033[0;33m',
                 'cyan': '\033[0;36m',
                 'resetcolor': '\033[0m'}

    if not color or color == 'nocolor':
        print(msg_text, end=end)
    else:
        try:
            print(color_dic[color] + msg_text + color_dic['resetcolor'],
                  end=end)
        except KeyError as exc:
            raise ValueError("Invalid color") from exc

    # flush stdout
    sys.stdout.flush()

    if exitcode:
        sys.exit(exitcode)


def print_table(header, rows, *, sortby='', alignl='', alignr='', hrules=''):
    """
    Print table using module prettytable.

    Arguments:
        header     (list): List with table header
        rows       (list): Nested list with table rows
                           [ [row1], [row2], [row3], ... ]

    Keyword arguments (optional):
        sortby      (str): header name to sort the output
        alignl     (list): headers name to align to left
        alignr     (list): headers name to align to right
        hrules      (str): Controls printing of horizontal rules after rows.
                           Allowed values: FRAME, HEADER, ALL, NONE

    Example:
    >>> header = ["col1", "col2"]
    >>> rows = [ ["line1_col1", "line1_col2"], ["line2_col1", "line2_col2"] ]
    >>> print_table(header, rows)
    +------------+------------+
    |    col1    |    col2    |
    +------------+------------+
    | line1_col1 | line1_col2 |
    | line2_col1 | line2_col2 |
    +------------+------------+
    """
    output = prettytable.PrettyTable(header)
    output.format = True
    if hrules:
        output.hrules = getattr(prettytable, hrules)

    for row in rows:
        if len(header) != len(row):
            raise ValueError("row does not have same size of header")
        row_entry = []
        for pos in row:
            row_entry.append(pos)
        output.add_row(row_entry)

    if sortby:
        # if sortby is invalid, ie, does not exist on header,
        # sort by first column by default
        output.sortby = sortby if sortby in header else header[0]
    for left in alignl:
        output.align[left] = 'l'
    for right in alignr:
        output.align[right] = 'r'

    print(output)


##############################################################################
##############################################################################
# Email
##############################################################################
##############################################################################


def send_email(mail_from, mail_to, subject, body,
               mailserver='localhost'):  # pragma: no cover
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
""" % (mail_from, mail_to, subject, body)

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
        logfile=None, *,
        filemode='a', date_format=None, log_level='DEBUG'):  # pragma: no cover
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
    dict_level = {'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}

    if log_level not in dict_level:
        raise ValueError("Invalid log_level")
    if filemode not in ['a', 'w']:
        raise ValueError("Invalid filemode")

    if not date_format:
        date_format = '%m/%d/%Y %H:%M:%S'

    log_fmt = '%(asctime)s %(module)s %(funcName)s %(levelname)s %(message)s'

    logging.basicConfig(level=dict_level[log_level],
                        format=log_fmt,
                        datefmt=date_format,
                        filemode=filemode,
                        filename=logfile)

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


def return_dict_value(
        dictionary, keys, *, ignore_key_error=False):  # pragma: no cover
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
                return ''
            raise
    else:
        # It is the last key, try to return the dict value for the key
        try:
            return dictionary[keys[0]]
        except (KeyError, TypeError):
            if ignore_key_error:
                return ''
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
        universal_newlines=True)

    # Poll process for new output until finished
    stdout_output = ""
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
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
# Bytes convertion
##############################################################################
##############################################################################

def bytes2human(size, *, unit='', precision=2, base=1024):
    """
    Convert number in bytes to human format.

    Arguments:
        size        (int): bytes to be converted

    Keyword arguments (opt):
        unit       (str): If it will convert bytes to a specific unit
                          'KB', 'MB', 'GB', 'TB', 'PB', 'EB'
        precision  (int): number of digits after the decimal point
        base       (int): 1000 - for decimal base
                          1024 - for binary base (it is the default)

    Returns:
        (int): number
        (str): unit ('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

    Exemple:
    >>> bytes2human(10)
    ('10.00', 'Bytes')
    >>> bytes2human(2048)
    ('2.00', 'KB')
    >>> bytes2human(27273042329)
    ('25.40', 'GB')
    >>> bytes2human(27273042329, precision=1)
    ('25.4', 'GB')
    >>> bytes2human(27273042329, unit='MB')
    ('26009.60', 'MB')
    """
    # validate parameters
    if not isinstance(precision, int):
        raise ValueError("precision is not a number")
    if not isinstance(base, int):
        raise ValueError("base is not a number")
    try:
        num = float(size)
    except ValueError:
        raise ValueError("value is not a number")

    suffix = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

    # If it needs to convert bytes to a specific unit
    if unit:
        try:
            num = num / base ** suffix.index(unit)
        except ValueError:
            raise ValueError("Error: unit must be {}".format(
                ", ".join(suffix[1:])))
        return "{0:.{prec}f}".format(num, prec=precision), unit

    # Calculate the greatest unit for the that size
    for counter, suffix_unit in enumerate(suffix):
        if num < base:
            return "{0:.{prec}f}".format(num, prec=precision), suffix_unit
        if counter == len(suffix)-1:
            raise ValueError("value greater than the highest unit")
        num /= base


def human2bytes(size, unit, *, precision=2, base=1024):
    """
    Convert size from human to bytes.

    Arguments:
        size       (int): number
        unit       (str): converts from this unit to bytes
                          'KB', 'MB', 'GB', 'TB', 'PB', 'EB'

    Keyword arguments (opt):
        precision  (int): number of digits after the decimal point
                          default is 2
        base       (int): 1000 - for decimal base
                          1024 - for binary base (it is the default)

    Returns:
        (int) number in bytes

    Example:
        >>> human2bytes(10, 'GB')
        '10737418240.00'
        >>> human2bytes(10, 'GB', precision=0)
        '10737418240'
        >>> human2bytes(10, 'PB')
        '11258999068426240.00'

    """
    dic_power = {'KB': base,
                 'MB': base ** 2,
                 'GB': base ** 3,
                 'TB': base ** 4,
                 'PB': base ** 5,
                 'EB': base ** 6,
                 'ZB': base ** 7}
    if unit not in dic_power:
        raise ValueError("invalid unit. It must be {}".format(
            ", ".join(dic_power.keys())))

    try:
        num_bytes = float(size) * int(dic_power[unit])
    except ValueError:
        raise ValueError("value is not a number")

    return "{0:.{prec}f}".format(num_bytes, prec=precision)


##############################################################################
##############################################################################
# Percentage Calculator
##############################################################################
##############################################################################

def pct_two_numbers(number1, number2, *, precision='2'):  # pragma: no cover
    """
    Calculate the percentage of number1 to number2.

    Number1 is what percent of number2

    Arguments:
        number1     (int): number
        number2     (int): number

    Keyword arguments (opt):
        precision   (int): number of digits after the decimal point
                           default is 2

    Returns:
        (str):  Pct value

    Example:
    >>> pct_two_numbers(30, 90)
    '33.33'
    >>> pct_two_numbers(30, 90, precision=0)
    '33'
    >>> pct_two_numbers(30, 90, precision=4)
    '33.3333'
    >>> pct_two_numbers(10, 50)
    '20.00'
    """
    try:
        num_pct = number1 * 100 / number2
        return "{0:.{prec}f}".format(num_pct, prec=precision)
    except ZeroDivisionError:
        return "{0:.{prec}f}".format(0, prec=precision)


def x_pct_of_number(pct, number, *, precision='2'):  # pragma: no cover
    """
    Calculate what is the x% of a number.

    Arguments:
        pct        (int): percentage
        number     (int): number

    Keyword arguments (opt):
        precision  (int): number of digits after the decimal point
                          default is 2

    Returns:
        (str):  number

    Exemple:
    >>> x_pct_of_number(33.333, 90)     # what is 33.333% of 90
    '30.00'
    >>> x_pct_of_number(40, 200)        # what is 40% of 200
    '80.00'
    >>> x_pct_of_number(40.9, 200)      # what is 40.9% of 200
    '81.80'
    >>> x_pct_of_number(40.9, 200, precision=4)
    '81.8000'
    >>> x_pct_of_number(40.9, 200, precision=0)
    '82'
    """
    num = number * pct / 100
    return "{0:.{prec}f}".format(num, prec=precision)


##############################################################################
##############################################################################
# Unix epoch time conversion
##############################################################################
##############################################################################

def epoch_time_to_human(
        epoch, *, date_format='%c', utc='no'):  # pragma: no cover
    """
    Convert a unix epoch time to human format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments:
        epoch       (int):    unix epoch time (timestamp)

    Keyword arguments (opt):
        date_format (str):    strftime format to show the epoch time
                              default is '%c' (Locale’s appropriate
                              date and time representation)
        utc         (yes/no): If unix epoch time in UTC timezone
                              default is no

    Example:
    >>> epoch_time_to_human(1530324373,date_format='%m%d%Y %H:%M:%S',utc='yes')
    '06302018 02:06:13'
    >>> epoch_time_to_human(1530324373) # doctest: +SKIP
    'Fri Jun 29 23:06:13 2018'
    >>> epoch_time_to_human(1530324373, utc='yes') # doctest: +SKIP
    'Sat Jun 30 02:06:13 2018'
    """
    if not isinstance(epoch, int):
        raise TypeError("epoch time must be int")

    if utc == 'yes':
        return datetime.datetime.utcfromtimestamp(epoch).strftime(date_format)

    return datetime.datetime.fromtimestamp(epoch).strftime(date_format)


def epoch_time_now(*, utc='no'):
    """
    Return current date and time in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments:
        utc         (yes/no): If returns unix epoch time in UTC timezone
                              default is no
    Example:
    >>> epoch_time_now() # doctest: +SKIP
    1530325275
    """
    if utc == 'yes':
        return int(datetime.datetime.utcnow().timestamp())
    elif utc == 'no':
        return int(datetime.datetime.now().timestamp())

    raise ValueError("error: epoch_time_now: utc is invalid")


def epoch_time_min_ago(minutes=5, *, utc='no'):
    """
    Return current date and time less x minutes in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        minutes  (int): Number of minutes ago to return unix timestamp
                        default is 5 minutes

    Keyword arguments (opt):
        utc         (yes/no): If unix epoch time in UTC timezone
                              default is no
    Example:
    >>> epoch_time_min_ago() # doctest: +SKIP
    1530325377
    >>> epoch_time_min_ago(30) # doctest: +SKIP
    1530323879
    """
    if not isinstance(minutes, int):
        raise TypeError("minutes must be int")

    return int(epoch_time_now(utc=utc) - (60 * minutes))


def epoch_time_hours_ago(hours=1, *, utc='no'):
    """
    Return current date and time with less x hours in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        hours     (int):    Number of hours ago to return unix timestamp
                            default is 1 hour

    Keyword arguments (opt):
        utc       (yes/no): If unix epoch time in UTC timezone
                            default is no
    Example:
    >>> epoch_time_hours_ago() # doctest: +SKIP
    1530322279
    >>> epoch_time_hours_ago(8) # doctest: +SKIP
    1530297083
    """
    if not isinstance(hours, int):
        raise TypeError("hours must be int")

    return int(epoch_time_now(utc=utc) - (hours * 3600))


def epoch_time_days_ago(days=1, *, utc='no'):
    """
    Return current date and time with less x days in unix epoch time format.

    Unix epoch time -  number of seconds that have elapsed since
                       00:00:00 Coordinated Universal Time (UTC),
                       1 January 1970

    Arguments (opt):
        days       (int):   Number of days ago to return unix timestamp
                            default is 1 day

    Keyword arguments (opt):
        utc       (yes/no): If unix epoch time in UTC timezone
                            default is no
    Example:
    >>> epoch_time_days_ago() # doctest: +SKIP
    1530239517
    >>> epoch_time_days_ago(7) # doctest: +SKIP
    1529721118
    """
    if not isinstance(days, int):
        raise TypeError("days must be int")

    return int(epoch_time_now(utc=utc) - (days * 24 * 3600))


##############################################################################
##############################################################################
# Date and Time conversion
##############################################################################
##############################################################################

def seconds_to_human(seconds, *, unit=None):
    """
    Convert number in seconds to human format.

    Arguments:
        seconds   (int):                               Number of seconds

    Keyword arguments (opt):
        unit      (Months/Days/Hours/Minutes/Seconds): Max unit used
                                                       to convert

    Example:
    >>> seconds_to_human(300)
    '5 Minutes'
    >>> seconds_to_human(310)
    '5 Minutes, 10 Seconds'
    >>> seconds_to_human(10810)
    '3 Hours, 10 Seconds'
    >>> seconds_to_human(10810, unit='Minutes')
    '180 Minutes, 10 Seconds'
    >>> seconds_to_human(180072)
    '2 Days, 2 Hours, 1 Minutes, 12 Seconds'
    >>> seconds_to_human(5191272)
    '2 Months, 2 Hours, 1 Minutes, 12 Seconds'
    """
    # 1 year = 365 days (60 * 60 * 24 * 365)
    # 1 month = 30 days (60 * 60 * 24 * 30)
    # 1 day    (60 * 60 * 24)
    # 1 hour   (60 * 60)
    # 1 minute (60)
    # 1 second
    seconds_list = [("Years", 31536000),
                    ("Months", 2592000),
                    ("Days", 86400),
                    ("Hours", 3600),
                    ("Minutes", 60),
                    ("Seconds", 1)]

    if not isinstance(seconds, int):
        raise TypeError("seconds must be int")

    if seconds == 0:
        return "0 Seconds"
    elif seconds < 0:
        raise TypeError(
            "error: seconds_to_human: seconds must be greater than 0")

    if unit:
        try:
            index = [a for a, b in enumerate(seconds_list) if b[0] == unit][0]
        except IndexError:
            raise TypeError("error: seconds_to_human: unit is invalid")
        seconds_list = seconds_list[index:]

    result = []
    for unit_name, unit_value_in_sec in seconds_list:
        num_unit = seconds // unit_value_in_sec
        if num_unit:
            seconds -= num_unit * unit_value_in_sec
            result.append("{} {}".format(num_unit, unit_name))
    return ", ".join(result)


def convert_datetime_to_tz(*, date, date_fmt,
                           from_tz='UTC', to_tz='America/Sao_Paulo'):
    """
    Convert a date to a specific timezone.

    Keyword arguments:

        date      (str):      date to convert
        date_fmt  (str):      format of the date to convert
        from_tz   (timezone): source timezone name (default: UTC)
        to_tz     (timezone): target timezone name (default: America/Sao_Paulo)

    Returns:
        datetime object with the target timezone defined.

    Example:
    # convert a date from utc to America/Sao_Paulo
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ")
    datetime.datetime(2019, 4, 26, 7, 38, 5,
                      tzinfo=<DstTzInfo 'America/Sao_Paulo' -03-1 day,
                      21:00:00 STD>)

    # convert date from America/Sao_Paulo to America/Los_Angeles
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ",
                               from_tz="America/Sao_Paulo",
                               to_tz="America/Los_Angeles")
    datetime.datetime(2019, 4, 26, 6, 38, 5, # doctest: +SKIP
                      tzinfo=<DstTzInfo 'America/Los_Angeles' PDT-1 day,
                      17:00:00 DST>)

    # Convert date from America/New_York to Asia/Dubai
    >>> convert_datetime_to_tz(date='2019-04-26T10:38:05Z', # doctest: +SKIP
                               date_fmt="%Y-%m-%dT%H:%M:%SZ",
                               from_tz="America/New_York",
                               to_tz="Asia/Dubai")
    datetime.datetime(2019, 4, 26, 18, 38, 5,
                      tzinfo=<DstTzInfo 'Asia/Dubai' +04+4:00:00 STD>)
    """
    # create datetime obj with date specified
    datetime_obj = datetime.datetime.strptime(date, date_fmt)
    # add timezone information to datetime obj
    datetime_obj_from = pytz.timezone(from_tz).localize(datetime_obj)
    # new datetime obj with target timezone
    datetime_obj_to = datetime_obj_from.astimezone(pytz.timezone(to_tz))

    return datetime_obj_to

# vim: ts=4
