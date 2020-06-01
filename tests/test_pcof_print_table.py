# -*- coding: utf-8 -*-
"""Test print_table function."""

import pytest
from pcof import pcof

header = ["col1", "col2", "mycol3"]
rows = [
        ["line1_col1", "line1_col2", "c_col3"],
        ["line2_col1", "line2_col2", "b_col3"],
        ["line3_col1", "line3_col2_test", "a_col3"],
       ]

def test_print_table(capsys):
    pcof.print_table(header, rows)
    result = """\
+------------+-----------------+--------+
|    col1    |       col2      | mycol3 |
+------------+-----------------+--------+
| line1_col1 |    line1_col2   | c_col3 |
| line2_col1 |    line2_col2   | b_col3 |
| line3_col1 | line3_col2_test | a_col3 |
+------------+-----------------+--------+
"""
    out, err = capsys.readouterr()
    assert out == result


def test_print_table_alignl(capsys):
    pcof.print_table(header, rows, alignl=["col2"])
    result = """\
+------------+-----------------+--------+
|    col1    | col2            | mycol3 |
+------------+-----------------+--------+
| line1_col1 | line1_col2      | c_col3 |
| line2_col1 | line2_col2      | b_col3 |
| line3_col1 | line3_col2_test | a_col3 |
+------------+-----------------+--------+
"""
    out, err = capsys.readouterr()
    assert out == result


def test_print_table_alignr(capsys):
    pcof.print_table(header, rows, alignr=["col2"])
    result = """\
+------------+-----------------+--------+
|    col1    |            col2 | mycol3 |
+------------+-----------------+--------+
| line1_col1 |      line1_col2 | c_col3 |
| line2_col1 |      line2_col2 | b_col3 |
| line3_col1 | line3_col2_test | a_col3 |
+------------+-----------------+--------+
"""
    out, err = capsys.readouterr()
    assert out == result


def test_print_table_hrules(capsys):
    pcof.print_table(header, rows, hrules="HEADER")
    result = """\
|    col1    |       col2      | mycol3 |
+------------+-----------------+--------+
| line1_col1 |    line1_col2   | c_col3 |
| line2_col1 |    line2_col2   | b_col3 |
| line3_col1 | line3_col2_test | a_col3 |
"""
    out, err = capsys.readouterr()
    assert out == result


def test_print_table_sort(capsys):
    pcof.print_table(header, rows, sortby="mycol3")
    result = """\
+------------+-----------------+--------+
|    col1    |       col2      | mycol3 |
+------------+-----------------+--------+
| line3_col1 | line3_col2_test | a_col3 |
| line2_col1 |    line2_col2   | b_col3 |
| line1_col1 |    line1_col2   | c_col3 |
+------------+-----------------+--------+
"""
    out, err = capsys.readouterr()
    assert out == result


def test_msg_error():
    row = [ ["col1", "col2" ] ]
    with pytest.raises(ValueError,
                       match="row does not have same size of header"):
        pcof.print_table(header, row)

# vim: ts=4
