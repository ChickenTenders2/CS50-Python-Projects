from numb3rs import validate

def test_validate_true():
    assert validate("255.255.255.255") == True

def test_validate_false():
    assert validate("255.255.255.512") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
