from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/4") == 0
    assert convert("1/100") == 1
    assert convert("2/4") == 50
    assert convert("99/100") == 99
    assert convert("4/4") == 100

def test_convert_errors():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
