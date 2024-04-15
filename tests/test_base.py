import os
import pprint
import sys

import pytest

from pythondevpractice import simple_functions

# import pythondevpractice.simple_functions as simple_functions

print("sys.path:")
pprint.pprint(sys.path)
print("Current working directory:", os.getcwd())


def test_plus(temp_num):
    a = temp_num[0]
    b = temp_num[1]
    assert (a + b) == simple_functions.plus(a, b)


@pytest.mark.parametrize("a,b", [(1, 2), (12, 63), (94, 33)])
def test_minus(a, b):
    assert (a - b) == simple_functions.minus(a, b)


def test_answer():
    # assert 3 == 5  # Assertion
    assert (1 + 2) == 3


# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x, "h is not in str"

    def test_two(self):
        x = "this"
        assert "s" in x
