"""Basic Unit testing for example.py"""

import math
from random import randint
import pytest
from example import increment, COLORS

def test_increment():
    """Testing increment function"""
    test_value = randint(0, 10)
    assert increment(3) == 4
    assert increment(-2) == -1
    assert increment(2.4) == 3.4
    for i in range(100):
        assert increment(test_value) == test_value + 1


def test_num_colors():
    """testing colors contents"""
    assert len(COLORS) ==4

def test_color_contents():
    assert 'blue' in COLORS
