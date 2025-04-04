from bank import value

def test_value_0():
    assert value("hello") == 0
    assert value("hello, world") == 0

def test_value_20():
    assert value("hi") == 20
    assert value("HOWDY") == 20

def test_value_100():
    assert value("What's up bro") == 100
    assert value("goodbye") == 100
