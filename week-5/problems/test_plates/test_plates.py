from plates import is_valid

def test_len():
    assert is_valid("A") == False
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("ABCDEFG") == False

def test_first_two():
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("AB") == True
    assert is_valid("A1B") == False

def test_first_digit():
    assert is_valid("AB1") == True
    assert is_valid("AB01") == False
    assert is_valid("AB1C") == False
    assert is_valid("AB12") == True

def test_punctuation():
    assert is_valid("AB!") == False
    assert is_valid("AB ") == False
    assert is_valid("AB@") == False
    assert is_valid("ABC") == True