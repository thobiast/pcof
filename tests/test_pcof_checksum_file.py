# -*- coding: utf-8 -*-
"""Test checksum_file function."""

import pytest
from pcof import pcof

@pytest.mark.parametrize("filename, algorithm, result", [
    ("tests/file_checksum.txt", "md5", "f978067032b567b197cef53a4d463a89"),
    ("tests/file_checksum.txt", "sha256", "f133e784590eae8c07dac9295ae50344731090dbfc848c1d77d0af4a79a56f21"),
])
def test_checksum_file(filename, algorithm, result):
    assert pcof.checksum_file(filename, algorithm=algorithm) == result

def test_checksum_file_raise():
    with pytest.raises(TypeError, match="hash algorithm not supported"):
        pcof.checksum_file("file", algorithm="hashnotexist")
    with pytest.raises(TypeError, match="block_size should be int"):
        pcof.checksum_file("file", block_size="10")

# vim: ts=4
