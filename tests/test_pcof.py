# -*- coding: utf-8 -*-

import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pcof

def test_bytes2human():
    assert pcof.bytes2human(10) == ('10.00', 'Bytes')
    assert pcof.bytes2human(27273042329) == ('25.40', 'GB')
    assert pcof.bytes2human(27273042329, precision=1) == ('25.4', 'GB')
    assert pcof.bytes2human(27273042329, unit='MB') == ('26009.60', 'MB')
    with pytest.raises(ValueError):
        pcof.bytes2human(27273042329, unit='MC')
    with pytest.raises(ValueError):
        pcof.bytes2human(27273042329, precision='12.1')
