import sys
import os
import pprint
print("sys.path:")
pprint.pprint(sys.path)
print("Current working directory:", os.getcwd())


# from pythondevpractice import simple_functions
import pythondevpractice.simple_functions as simple_functions


def test_plus():
    a = 1
    b = 2
    assert (a + b) == simple_functions.plus(a, b)


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
