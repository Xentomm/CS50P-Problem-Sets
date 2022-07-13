from seasons import check_birthday

def main():
    test_check_birthday()

def test_check_birthday():
    assert check_birthday('1999-10-26') == ("1999", "10", "26")
    assert check_birthday('1999-1-6') == None
    assert check_birthday('October 26, 1999') == None 

if __name__ == "__main__":
    main()