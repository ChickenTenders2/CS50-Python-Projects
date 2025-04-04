import pytest
from seasons import Age
from datetime import datetime

def test_age_in_words():
    birthdate = datetime.strptime("2020-01-01", "%Y-%m-%d").date()
    age = Age(birthdate)
    assert age.age_in_words() == "Two million, four hundred sixty-three thousand, eight hundred forty minutes"

def test_age_failed():
    with pytest.raises(ValueError):
        datetime.strptime("January 1, 2020", "%Y-%m-%d").date()
