import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from second import processing_names


def test_processing_name():
    assert processing_names(['MAY']) == 39
    assert processing_names(['someName']) == 85


