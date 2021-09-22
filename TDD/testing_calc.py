import pytest
import calc

def test_add():
    expected = 10
    actual = calc.add(5, 5)
    assert(actual == expected)

def test_sub():
    expected = 0
    actual = calc.sub(5, 5)
    assert(actual == expected)

def test_mult():
    expected = 25
    actual = calc.mult(5, 5)
    assert(actual == expected)

def test_div():
    expected = 1
    actual = calc.divide(5, 5)
    assert(actual == expected)

def test_all():
    test_add()
    test_sub()
    test_mult()
    test_div()

test_all()