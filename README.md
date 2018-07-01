Help on module pcof:

NAME
    pcof - Python Collection Of Functions

DESCRIPTION
    This module has a collection of many small generic useful functions.
    
    Developed for Python 3

FUNCTIONS
    bytes2human(size, *, unit='', precision=2, base=1024)
        Convert number in bytes to human format
        
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
            (str): unit (Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
        
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
    
    epoch_time_days_ago(days=1, *, utc='no')
        Return current date and time with less x days in unix epoch time format
        
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
        >>> epoch_time_days_ago()
        1530239517
        >>> epoch_time_days_ago(7)
        1529721118
    
    epoch_time_hours_ago(hours=1, *, utc='no')
        Return current date and time with less x hours in unix epoch time format
        
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
        >>> epoch_time_hours_ago()
        1530322279
        >>> epoch_time_hours_ago(8)
        1530297083
    
    epoch_time_min_ago(minutes=5, *, utc='no')
        Return current date and time less x minutes in unix epoch time format
        
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
        >>> epoch_time_min_ago()
        1530325377
        >>> epoch_time_min_ago(30)
        1530323879
    
    epoch_time_now(*, utc='no')
        Return current date and time in unix epoch time format
        
        Unix epoch time -  number of seconds that have elapsed since
                           00:00:00 Coordinated Universal Time (UTC),
                           1 January 1970
        
        Arguments:
            utc         (yes/no): If returns unix epoch time in UTC timezone
                                  default is no
        Example:
        >>> epoch_time_now()
        1530325275
    
    epoch_time_to_human(epoch, *, date_format='%c', utc='no')
        Convert a unix epoch time to human format
        
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
        >>> epoch_time_to_human(1530324373,'%m/%d/%Y %H:%M:%S')
        '06/29/2018 23:06:13'
        >>> epoch_time_to_human(1530324373)
        'Fri Jun 29 23:06:13 2018'
        >>> epoch_time_to_human(1530324373, utc='yes')
        'Sat Jun 30 02:06:13 2018'
    
    human2bytes(size, unit, *, precision=2, base=1024)
        Convert size from human to bytes
        
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
    
    msg(color, msg_text, exitcode=0, *, mail_from=None, mail_to=None, mail_server='localhost', subject=None)
        Print colored text.
        
        Arguments:
            size      (str): color name (blue, red, green, yellow,
                                         cyan or nocolor)
            msg_text  (str): text to be printed
            exitcode  (int, opt): Optional parameter. If exitcode is different
                                  from zero, it terminates the script, i.e,
                                  it calls sys.exit with the exitcode informed
        
        Keyword arguments to send the msg_text by email too:
            mail_from   (str, opt): send email from this address
            mail_to     (str, opt): send email to this address
            subject     (str, opt): mail subject
            mail_server (str, opt): mail server address
        
        Exemplo:
            msg("blue", "nice text in blue")
            msg("red", "Error in my script.. terminating", 1)
    
    nested_dict()
        Returns a nested dictionary, i.e, an dictionary with
        arbitrary number of levels.
        
        Example:
        >>> mydict = nested_dict()
        >>> mydict['aa']['bb']['cc'] = 'teste'
        >>> print(mydict)
             defaultdict(<function nested_dict at 0x7f1e74b8bea0>, {'aa':
             defaultdict(<function nested_dict at 0x7f1e74b8bea0>, {'bb':
             defaultdict(<function nested_dict at 0x7f1e74b8bea0>, {'cc':
             'teste'})})})
        >>> import pprint
        >>> pprint.pprint(mydict)
             {'aa': {'bb': {'cc': 'teste'}}}
    
    pct_two_numbers(number1, number2, *, precision='2')
        Calculate the percentage of number1 to number2, i.e,
        number1 is what percent of number2
        
        Arguments:
            number1 (int): number
            number2 (int): number
        
        Keyword arguments (opt):
            precision  (int): number of digits after the decimal point
                              default is 2
        
        Returns:
            (int): Pct value
        
        Example:
        >>> pct_two_numbers(30, 90)
        '33.33'
        >>> pct_two_numbers(30, 90, precision=0)
        '33'
        >>> pct_two_numbers(30, 90, precision=4)
        '33.3333'
        >>> pct_two_numbers(10, 50)
        '20.00'
    
    run_cmd(cmd)
        Execute a command on the operating system
        
        Arguments:
            cmd    (str): the command to be executed
        
        Return:
            - If command complete with return code zero
            return: command_return_code, stdout
        
            - If command completes with return code different from zero
            return: command_return_code, stderr
    
    send_email(mail_from, mail_to, subject, body, mailserver='localhost')
        Send an email using smtplib module
        
        Arguments:
            mail_from   (str): send email from this address
            mail_to     (str): send email to this address
            subject     (str): mail subject
            mail_server (str, opt): mail server address. Default is localhost
    
    setup_logging(logfile=None, *, filemode='a', date_format=None, log_level='DEBUG')
        Configure logging
        
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
    
    x_pct_of_number(pct, number, *, precision='2')
        Calculate what is the x% of a number
        
        Arguments:
            pct        (int): percentage
            number     (int): number
        
        Keyword arguments (opt):
            precision  (int): number of digits after the decimal point
                              default is 2
        
        Returns:
            (int):  number
        
        Exemple:
        >>> x_pct_of_number(33.333, 90)     # what is 33.333% of 90
        '30.00'
        >>> x_pct_of_number(40, 200)        # what is 40% of 200
        '80.00'
        >>> x_pct_of_number(40.9, 200)      # what is 40.9* of 200
        '81.80'
        >>> x_pct_of_number(40.9, 200, precision=4)
        '81.8000'
        >>> x_pct_of_number(40.9, 200, precision=0)

FILE
    /home/thobias/repo/pcof/pcof.py


