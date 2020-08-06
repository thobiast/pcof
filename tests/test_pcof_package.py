# -*- coding: utf-8 -*-
"""Test package metadata."""

import pytest
import pcof


def test_metadata():
    """Test module metadata attribute."""
    assert "http" in pcof.__url__
    assert pcof.__license__ == "MIT"
    assert pcof.__name__ == "pcof"
    assert isinstance(pcof.__version__, str)
    assert isinstance(pcof.__description__, str)
    assert isinstance(pcof.__author__, str)


# vim: ts=4
