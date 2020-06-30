import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from third import get_zeros


def test_get_zeros():
    assert get_zeros(25) == 6
    assert get_zeros(12) == 2
    assert get_zeros(5) == 1
    assert get_zeros(40) == 9
