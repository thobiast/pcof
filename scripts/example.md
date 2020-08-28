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

