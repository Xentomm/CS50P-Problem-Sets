import bank

def main():
    test_value_hello()
    test_value_h()
    test_value_no_h()


def test_value_hello():
    assert bank.value("hello") == "$0"

def test_value_h():
    assert bank.value("hi") == "$20"

def test_value_no_h():
    assert bank.value("welcome") == "$100"

if __name__ == "__main__":
    main()