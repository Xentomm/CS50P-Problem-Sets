from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"cat") == False
    assert validate(r"255.255.255") == False
    assert validate(r"255.255,255.255") == False
    assert validate(r"255.255.255.255") == True

def test_range():
    assert validate(r"100.100.100.256") == False
    assert validate(r"100.100.256.100") == False
    assert validate(r"100.256.100.100") == False
    assert validate(r"256.100.100.100") == False
    assert validate(r"255.100.100.100") == True

if __name__ == "__main__":
    main()