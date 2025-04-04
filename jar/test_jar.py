import pytest
from jar import Jar

def test_jar_status():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12

def test_Jar_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_jar_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

def test_jar_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(4)
    assert jar.size == 1


