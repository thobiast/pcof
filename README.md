# pcof - Python Collection Of Functions

![Build Status](https://github.com/thobiast/pcof/workflows/build/badge.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pcof)
![PyPI](https://img.shields.io/pypi/v/pcof)
[![codecov](https://codecov.io/gh/thobiast/pcof/branch/master/graph/badge.svg)](https://codecov.io/gh/thobiast/pcof)
[![GitHub License](https://img.shields.io/github/license/thobiast/pcof)](https://github.com/thobiast/pcof/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pcof is a collection of small useful functions.

## Installation

```bash
pip install pcof
```

Most of the functions do not have any external dependencies.
If your script does not use any pcof function with dependencies, then you can
install pcof and ignore its dependencies.

```bash
pip install --no-deps pcof
```

## Usage Example

```python
>>> from pcof import bytesconv

>>> bytesconv.bytes2human(88191837473)
('82.14', 'GB')
>>> bytesconv.bytes2human(88191837473, unit='MB')
('84106.29', 'MB')
>>> bytesconv.bytes2human(88191837473, unit='MB', precision=0)
('84106', 'MB')

>>> bytesconv.human2bytes(100, 'GB')
'107374182400.00'
>>> bytesconv.human2bytes(100, 'GB', base=1000)
'100000000000.00'

>>> bytesconv.bandwidth_converter(100, from_unit="Mbps", to_unit="MB")
(12.5, 'MB/seconds')
>>> bytesconv.bandwidth_converter(10, from_unit="Gbps", from_time="seconds", to_unit="GB", to_time="minutes")
(75.0, 'GB/minutes')
>>> bytesconv.bandwidth_converter(6, from_unit="GB", from_time="hours", to_unit="Mbps", to_time="seconds")
(13.333333333333334, 'Mbps/seconds')

>>> from pcof import datetimefunc

>>> datetimefunc.epoch_time_now()
1591041372
>>> datetimefunc.epoch_time_min_ago(60)
1591037781
>>> datetimefunc.epoch_time_hours_ago(12)
1590998197
>>> datetimefunc.epoch_time_days_ago(30)
1588449403

>>> datetimefunc.epoch_time_to_human(1590175926)
'Fri May 22 16:32:06 2020'
>>> datetimefunc.epoch_time_to_human(1590175926, utc='yes', date_format='%m/%d/%Y %H:%M:%S')
'05/22/2020 19:32:06'

>>> datetimefunc.seconds_to_human(300)
'5 Minutes'
>>> datetimefunc.seconds_to_human(310)
'5 Minutes, 10 Seconds'
>>> datetimefunc.seconds_to_human(8481083)
'3 Months, 8 Days, 3 Hours, 51 Minutes, 23 Seconds'

>>> datetimefunc.time_unit_conversion(90, from_unit="days", to_unit="months")
'3'

>>> from pcof.pct import x_pct_of_number
>>> x_pct_of_number(40, 200) # 40% of 200
'80.00'

>>> from pcof import printtable
>>> header = ["col1", "col2"]
>>> rows = [ ["line1_col1", "line1_col2"], ["line2_col1", "line2_col2"] ]
>>> pcof.print_table(header, rows)
    +------------+------------+
    |    col1    |    col2    |
    +------------+------------+
    | line1_col1 | line1_col2 |
    | line2_col1 | line2_col2 |
    +------------+------------+

>>> from pcof import misc
>>> misc.checksum_file("tests/file_checksum.txt")
'f133e784590eae8c07dac9295ae50344731090dbfc848c1d77d0af4a79a56f21'
>>> misc.checksum_file("tests/file_checksum.txt", algorithm='md5')
'f978067032b567b197cef53a4d463a89'

>>> import time
>>> from pcof import decorators
>>> @decorators.time_elapsed(print_info=True)
... def myfunc():
...    time.sleep(1)
...
>>> myfunc()
Decorator time_elapsed: myfunc args: () kwargs: {} -  elapsed time 1.0012 seconds. This function all execution elapsed time: 1.0012 seconds
>>> myfunc()
Decorator time_elapsed: myfunc args: () kwargs: {} -  elapsed time 1.0011 seconds. This function all execution elapsed time: 2.0023 seconds

>>> from pcof.downloadfile import download_file
>>> download_file("http://google.com/favicon.ico", "/tmp/google.ico")
```

## List of available functions

### Functions

| Module | Name | Description | Dependencies |
|:-------|:-----|:------------|:-------------|
| misc | msg |  Print colored text. | - |
| misc | send_email |  Send an email using smtplib module. | - |
| misc | setup_logging |  Configure logging. | - |
| misc | nested_dict |  Return a nested dictionary (arbitrary number of levels). | - |
| misc | find_key |  Return a value for a key in a dictionary. | - |
| misc | return_dict_value |  Return a value from a dictionary. | - |
| misc | run_cmd |  Execute a command on the operating system. | - |
| misc | checksum_file |  Return checksums (hash) of a file. | - |
| bytesconv | bytes2human |  Convert number in bytes to human format. | - |
| bytesconv | human2bytes |  Convert size from human to bytes. | - |
| bytesconv | bandwidth_converter |  Bandwidth Calculator. | - |
| datetimefunc | epoch_time_to_human |  Convert a unix epoch time to human format. | - |
| datetimefunc | epoch_time_now |  Return current date and time in unix epoch time format. | - |
| datetimefunc | epoch_time_min_ago |  Return current date and time less x minutes in unix epoch time format. | - |
| datetimefunc | epoch_time_hours_ago |  Return current date and time with less x hours in unix epoch time format. | - |
| datetimefunc | epoch_time_days_ago |  Return current date and time with less x days in unix epoch time format. | - |
| datetimefunc | time_unit_conversion |  Convert number from a time unit to another time unit. | - |
| datetimefunc | seconds_to_human |  Convert number in seconds to human format. | - |
| pct | y_what_pct_of_x |  Calculate the percentage of number1 to number2. | - |
| pct | x_pct_of_number |  Calculate what is the x% of a number. | - |
| pct | pct_change_from_x_to_y |  Calculate percent increase/decrease from number1 to number2. | - |
| printtable | print_table |  Print table using module prettytable. | prettytable |
| pytz | convert_datetime_to_tz |  Convert a date to a specific timezone. | pytz |
| downloadfile | download_file |  Download a file. | requests |

### Decorators

| Module | Name | Description | Dependencies |
|:-------|:-----|:------------|:-------------|
| decorators | num_calls |  Count the number of times a function is called. | - |
| decorators | time_elapsed |  Calculate elapsed time in seconds. | - |
| decorators | debug |  Show function parameters and return values. | - |
| decorators | retry_on_exception |  Retry function execution if exception raises. | - |

## Documentation (automatically generated using pydoc)

```
Help on module misc:

NAME
    misc - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Miscellaneous functions

FUNCTIONS
```

```python
    checksum_file(filename, *, algorithm='sha256', block_size=1048576)
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

    find_key(dict_obj, key)
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

    msg(color, msg_text, exitcode=0, *, end='\n', flush=True, output=None)
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

    nested_dict()
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

    return_dict_value(dictionary, keys, *, ignore_key_error=False)
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

    run_cmd(cmd)
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

    send_email(mail_from, mail_to, subject, body, mailserver='localhost')
        Send an email using smtplib module.

        Arguments:
            mail_from        (str): send email from this address
            mail_to          (str): send email to this address
            subject          (str): mail subject
            mail_server (str, opt): mail server address. Default is localhost

    setup_logging(logfile=None, *, filemode='a', date_format=None, log_level='DEBUG')
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

```
```
Help on module bytesconv:

NAME
    bytesconv - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Bytes calculator

FUNCTIONS
```

```python
    bandwidth_converter(number, *, from_unit, to_unit, from_time='seconds', to_time='seconds')
        Bandwidth Calculator.

        Convert data rate from one unit to another.

        Arguments:
            number     (int): number to be converted

        Keyword arguments:
            from_unit  (str): convert from this data unit. Example:
                              (bps, Kbps, Mbps, Gbps... KB, KiB, MB, MiB...)
            to_unit    (str): convert to this data unit. Example:
                              (bps, Kbps, Mbps, Gbps... KB, KiB, MB, MiB...)

        Keyword arguments (opt):
            from_time  (str): Specify the time frame used in from_unit
                              (seconds, minutes, hours, days, months)
                              default: seconds
            to_time    (str): Specify the time frame used in to_unit
                              (seconds, minutes, hours, days, months)
                              default: seconds

        bps, Kbps, Mbps, Gbps... = decimal base = 1000^n
        KB, MB, GB, TB...        = decimal base = 1000^n
        KiB, MiB, GiB, TiB...    = binary base  = 1024^n

        References:
            - https://en.wikipedia.org/wiki/Units_of_information
            - https://physics.nist.gov/cuu/Units/binary.html

        Returns: tuple
           (number_converted, to_unit/to_time)

        Example:
        >>> bandwidth_converter(100, from_unit="Mbps", to_unit="MB")
        (12.5, 'MB/seconds')
        >>> bandwidth_converter(100, from_unit="Mbps", to_unit="GB", to_time="hours")
        (45.0, 'GB/hours')
        >>> bandwidth_converter(1, from_unit="Gbps", to_unit="MB")
        (125.0, 'MB/seconds')
        >>> bandwidth_converter(10, from_unit="Gbps", to_unit="GB")
        (1.25, 'GB/seconds')
        >>> bandwidth_converter(10, from_unit="Gbps", to_unit="TB", to_time="hours")
        (4.5, 'TB/hours')
        >>> bandwidth_converter(10, from_unit="GB", to_unit="Gbps")
        (80.0, 'Gbps/seconds')
        >>> Convert 2.25 GB per hours to Mbps # doctest: +SKIP
        >>> bandwidth_converter(2.25, from_unit="GB", from_time="hours", to_unit="Mbps", to_time="seconds") # noqa
        (5.0, 'Mbps/seconds')

    bytes2human(size, *, unit='', precision=2, base=1024)
        Convert number in bytes to human format.

        Arguments:
            size       (int): bytes to be converted

        Keyword arguments (opt):
            unit       (str): If it will convert bytes to a specific unit
                              'KB', 'MB', 'GB', 'TB', 'PB', 'EB'
            precision  (int): number of digits after the decimal point
            base       (int): 1000 - for decimal base
                              1024 - for binary base (it is the default)

        Returns:
            (int): number
            (str): unit ('Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']

        Example:
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

    human2bytes(size, unit, *, precision=2, base=1024)
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

```
```
Help on module datetimefunc:

NAME
    datetimefunc - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Date and time functions

FUNCTIONS
```

```python
    epoch_time_days_ago(days=1, *, utc='no')
        Return current date and time with less x days in unix epoch time format.

        Unix epoch time -  number of seconds that have elapsed since
                           00:00:00 Coordinated Universal Time (UTC),
                           1 January 1970

        Arguments (opt):
            days         (int): Number of days ago to return unix timestamp
                                default is 1 day

        Keyword arguments (opt):
            utc       (yes/no): If unix epoch time in UTC timezone
                                default is no
        Example:
        >>> epoch_time_days_ago() # doctest: +SKIP
        1530239517
        >>> epoch_time_days_ago(7) # doctest: +SKIP
        1529721118

    epoch_time_hours_ago(hours=1, *, utc='no')
        Return current date and time with less x hours in unix epoch time format.

        Unix epoch time -  number of seconds that have elapsed since
                           00:00:00 Coordinated Universal Time (UTC),
                           1 January 1970

        Arguments (opt):
            hours        (int): Number of hours ago to return unix timestamp
                                default is 1 hour

        Keyword arguments (opt):
            utc       (yes/no): If unix epoch time in UTC timezone
                                default is no
        Example:
        >>> epoch_time_hours_ago() # doctest: +SKIP
        1530322279
        >>> epoch_time_hours_ago(8) # doctest: +SKIP
        1530297083

    epoch_time_min_ago(minutes=5, *, utc='no')
        Return current date and time less x minutes in unix epoch time format.

        Unix epoch time -  number of seconds that have elapsed since
                           00:00:00 Coordinated Universal Time (UTC),
                           1 January 1970

        Arguments (opt):
            minutes        (int): Number of minutes ago to return unix timestamp
                            default is 5 minutes

        Keyword arguments (opt):
            utc         (yes/no): If unix epoch time in UTC timezone
                                  default is no
        Example:
        >>> epoch_time_min_ago() # doctest: +SKIP
        1530325377
        >>> epoch_time_min_ago(30) # doctest: +SKIP
        1530323879

    epoch_time_now(*, utc='no')
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

    epoch_time_to_human(epoch, *, date_format='%c', utc='no')
        Convert a unix epoch time to human format.

        Unix epoch time -  number of seconds that have elapsed since
                           00:00:00 Coordinated Universal Time (UTC),
                           1 January 1970

        Arguments:
            epoch          (int): unix epoch time (timestamp)

        Keyword arguments (opt):
            date_format    (str): strftime format to show the epoch time
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

    seconds_to_human(seconds, *, unit=None)
        Convert number in seconds to human format.

        Arguments:
            seconds      (int): Number of seconds

        Keyword arguments (opt):
            unit         (Months/Days/Hours/Minutes/Seconds):
                                Max unit used to convert

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

    time_unit_conversion(number, *, from_unit, to_unit, precision=0, days_month=30, days_year=365)
        Convert number from a time unit to another time unit.

        Arguments:
            number             (int): number to convert

        Keyword arguments:
            from_unit    (seconds/minutes/hours/days/weeks/months/years):
                                      unit to convert from
            to_unit      (seconds/minutes/hours/days/weeks/months/years):
                                      unit to convert to

        Keyword arguments (opt):
            precision          (int): number of digits after the decimal point
                                      (default 0)
            days_month   (int/float): number of days in each month
                                      (default 30)
            days_year    (int/float): number of days in each year
                                      (default 365)

        Return:
            number converted to new unit

        Example:
        >>> time_unit_conversion(3600, from_unit="seconds", to_unit="hours")
        '1'
        >>> time_unit_conversion(1400, from_unit="minutes", to_unit="days")
        '1'
        >>> time_unit_conversion(36, from_unit="hours", to_unit="days", precision=1)
        '1.5'
        >>> time_unit_conversion(90, from_unit="days", to_unit="months")
        '3'

```
```
Help on module pct:

NAME
    pct - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Percentage Calculator

FUNCTIONS
```

```python
    pct_change_from_x_to_y(number1, number2, *, precision='2')
        Calculate percent increase/decrease from number1 to number2.

        Arguments:
            number1    (int): start value (from)
            number2    (int): end value (to)

        Keyword arguments (opt):
            precision  (int): number of digits after the decimal point
                              default is 2

        Returns:
            (str):  number

        Example:
        >>> pct_change_from_x_to_y(100, 110)  # what is the pct increase from 100 to 110?
        '10.00%'
        >>> pct_change_from_x_to_y(100, 90)   # what is the pct from 100 to 90?
        '-10.00%'
        >>> pct_change_from_x_to_y(25, 50, precision=0)
        '100%'

    x_pct_of_number(pct, number, *, precision='2')
        Calculate what is the x% of a number.

        Arguments:
            pct        (int): percentage
            number     (int): number

        Keyword arguments (opt):
            precision  (int): number of digits after the decimal point
                              default is 2

        Returns:
            (str):  number

        Example:
        >>> x_pct_of_number(33.333, 90)     # what is 33.333% of 90?
        '30.00'
        >>> x_pct_of_number(40, 200)        # what is 40% of 200?
        '80.00'
        >>> x_pct_of_number(40.9, 200)      # what is 40.9% of 200?
        '81.80'
        >>> x_pct_of_number(40.9, 200, precision=4)
        '81.8000'
        >>> x_pct_of_number(40.9, 200, precision=0)
        '82'

    y_what_pct_of_x(number1, number2, *, precision='2')
        Calculate the percentage of number1 to number2.

        Number1 is what percent of number2.

        Arguments:
            number1     (int): number
            number2     (int): number

        Keyword arguments (opt):
            precision   (int): number of digits after the decimal point
                               default is 2

        Returns:
            (str):  Pct value

        Example:
        >>> y_what_pct_of_x(30, 90)    # 30 is what percent of 90?
        '33.33%'
        >>> y_what_pct_of_x(30, 90, precision=0)
        '33%'
        >>> y_what_pct_of_x(30, 90, precision=4)
        '33.3333%'
        >>> y_what_pct_of_x(10, 50, precision=0) # 10 is what percent of 50?
        '20%'

```
```
Help on module printtable:

NAME
    printtable - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Dependencies: prettytable

FUNCTIONS
```

```python
    print_table(header, rows, *, sortby='', alignl='', alignr='', hrules='')
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

```
```
Help on module pytz:

NAME
    pytz - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Dependencies: pytz

FUNCTIONS
```

```python
    convert_datetime_to_tz(*, date, date_fmt, from_tz='UTC', to_tz='America/Sao_Paulo')
        Convert a date to a specific timezone.

        Keyword arguments:

            date           (str): date to convert
            date_fmt       (str): format of the date to convert
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

```
```
Help on module downloadfile:

NAME
    downloadfile - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Dependencies: requests

FUNCTIONS
```

```python
    download_file(url, local_file, *, allow_redirects=True, decode=True)
        Download a file.

        Arguments:
            url                    (str): URL to download
            local_file             (str): Local filename to store the downloaded
                                          file

        Keyword arguments (opt):
            allow_redirects (True/False): Allow request to redirect url
                                          default: True
            decode          (True/False): Decode compressed responses like gzip
                                          default: True

        Return:
            Request response headers

        Example:
        >>> download_file("http://google.com/favicon.ico", # doctest: +SKIP
                          "/tmp/google.ico")

```

```
Help on module decorators:

NAME
    decorators - Python Collection Of Functions.

DESCRIPTION
    Package with collection of small useful functions.

    Decorators functions

FUNCTIONS
```

```python
    debug(_func=None, *, loglevel='DEBUG', print_info=False)
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

    num_calls(_func=None, *, loglevel='DEBUG', print_info=False)
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

    retry_on_exception(_func=None, *, exception=(<class 'Exception'>,), loglevel='DEBUG', max_retry=5, sleep_retry=1, exception_error=None)
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

    time_elapsed(_func=None, *, loglevel='DEBUG', print_info=False)
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

```
