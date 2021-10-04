"""
Testing suite for practice practical for GCIS 123
"""

import practice

def test_gen_number():
    expected = True
    if 0 <= practice.gen_number() <= 5:
        actual = True
    else:
        actual = False 
    
    # assert(0 <= practice.gen_number() <= 5) also works
    assert(expected == actual)

def test_get_color():
    expected = "black"
    actual = practice.get_color(0)
    assert(expected ==  actual)

def test_draw_square():
    expected = 400
    actual = practice.draw_square(100)
    assert(expected == actual)

def test_draw_line():
    expected = 2000
    actual = practice.draw_line(5, 100)
    assert(expected == actual)

def test_all():
    test_gen_number()
    test_get_color()
    test_draw_square()
    test_draw_line()

test_all()