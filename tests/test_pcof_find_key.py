# -*- coding: utf-8 -*-
"""Test find_key function."""

import pytest
from pcof import pcof

DICT_1 = {
          "A1": "A",
          "B1": "B",
          "C1": {
                  "A2": "AA",
                  "B2": "BB",
                  "C2": { "A3": "AAA"},
                  "D1": "DD"
                },
          "D1": "D",
          "E1": ["E"],
          "F1": ["F", "FF"],
          "G1": [ {"G2": "G"},
                  {"G2": "GG"}
                ]
         }

@pytest.mark.parametrize("key, result", [
    ("A1", ["A"]),
    ("A2", ["AA"]),
    ("C1", [{'A2': 'AA', 'B2': 'BB', 'C2': {'A3': 'AAA'}, 'D1': 'DD'}]),
    ("C2", [{'A3': 'AAA'}]),
    ("A3", ["AAA"]),
    ("D1", ["DD", "D"]),
    ("E1", [["E"]]),
    ("F1", [["F", "FF"]]),
    ("G2", ["G", "GG"]),
])
def test_find_key(key, result):
    assert pcof.find_key(DICT_1, key) == result

# vim: ts=4
