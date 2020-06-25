```python
>>> from pcof import pcof

>>> pcof.bytes2human(88191837473)
('82.14', 'GB')
>>> pcof.bytes2human(88191837473, unit='MB')
('84106.29', 'MB')
>>> pcof.bytes2human(88191837473, unit='MB', precision=0)
('84106', 'MB')

>>> pcof.human2bytes(100, 'GB')
'107374182400.00'

>>> pcof.epoch_time_now()
1591041372
>>> pcof.epoch_time_min_ago(60)
1591037781
>>> pcof.epoch_time_hours_ago(12)
1590998197
>>> pcof.epoch_time_days_ago(30)
1588449403

>>> pcof.epoch_time_to_human(1590175926)
'Fri May 22 16:32:06 2020'
>>> pcof.epoch_time_to_human(1590175926, utc='yes', date_format='%m/%d/%Y %H:%M:%S')
'05/22/2020 19:32:06'

>>> pcof.x_pct_of_number(40, 200) # 40% of 200
'80.00'

>>> pcof.seconds_to_human(300)
'5 Minutes'
>>> pcof.seconds_to_human(310)
'5 Minutes, 10 Seconds'
>>> pcof.seconds_to_human(8481083)
'3 Months, 8 Days, 3 Hours, 51 Minutes, 23 Seconds'

>>> header = ["col1", "col2"]
>>> rows = [ ["line1_col1", "line1_col2"], ["line2_col1", "line2_col2"] ]
>>> pcof.print_table(header, rows)
    +------------+------------+
    |    col1    |    col2    |
    +------------+------------+
    | line1_col1 | line1_col2 |
    | line2_col1 | line2_col2 |
    +------------+------------+

>>> pcof.checksum_file("tests/file_checksum.txt")
'f133e784590eae8c07dac9295ae50344731090dbfc848c1d77d0af4a79a56f21'
>>> pcof.checksum_file("tests/file_checksum.txt", algorithm='md5')
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
```

