import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from first import search_pairs, search_pairs_pythonic


def test_search_pairs():
    assert search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5) == [(1, 4), (2, 3)]
    assert search_pairs([-1, 1, 2, 5, 6], 1) == [(-1, 2)]
    assert search_pairs([1, 2, 4], 2) == []
    assert search_pairs([-5, 12, -3, 4, -1, 1, 2, 5, 6], 7) == [(-5, 12), (1, 6), (2, 5)]
    assert search_pairs([-1, -3, 4, -8, -8], -4) == [(-1, -3), (4, -8)]


def test_search_pairs_pythonic():
    assert search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5) == [(1, 4), (2, 3)]
    assert search_pairs([-1, 1, 2, 5, 6], 1) == [(-1, 2)]
    assert search_pairs([1, 2, 4], 2) == []
    assert search_pairs([-5, 12, -3, 4, -1, 1, 2, 5, 6], 7) == [(-5, 12), (1, 6), (2, 5)]
    assert search_pairs([-1, -3, 4, -8, -8], -4) == [(-1, -3), (4, -8)]
