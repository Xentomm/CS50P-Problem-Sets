from plates import is_valid

def main():
    test_is_valid()

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_is_valid_wrong():
    assert is_valid("CS20") == True


if __name__ == "__main__":
    main()
