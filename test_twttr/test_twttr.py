from twttr import shorten

def test_shorten():
    assert shorten("Hello World") == "Hll Wrld"

def test_shorten_upper():
    assert shorten("HELLO WORLD") == "HLL WRLD"

def test_shorten_punctuation():
    assert shorten("Hello World!") == "Hll Wrld!"

def test_shorten_numbers():
    assert shorten("Hello World 123") == "Hll Wrld 123"
