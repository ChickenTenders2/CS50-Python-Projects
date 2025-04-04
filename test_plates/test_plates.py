from plates import is_valid

def test_valid_letters():
    assert is_valid("HELLO") == True

def test_valid_combination():
    assert is_valid("AAA222") == True
    assert is_valid("CS50") == True

def test_invalid_letters():
    assert is_valid("GOODBYE") == False

def test_invalid_combination():
    assert is_valid("AAA22A") == False
    assert is_valid("AAA22@") == False
    assert is_valid("CS05") == False

def test_invalid_numbers():
    assert is_valid("50") == False
