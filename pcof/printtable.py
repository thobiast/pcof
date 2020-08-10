# -*- coding: utf-8 -*-
"""
Python Collection Of Functions.

Package with collection of small useful functions.

Dependencies: prettytable
"""

import prettytable


def print_table(header, rows, *, sortby="", alignl="", alignr="", hrules=""):
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
        output.align[left] = "l"
    for right in alignr:
        output.align[right] = "r"

    print(output)


# vim: ts=4
