from um import count

def test_count():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Hello!") == 0

