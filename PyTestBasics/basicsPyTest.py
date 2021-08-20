import pytest

# start with test_ or _test  end with

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a ==b , "test failed as a is not equal to b"
