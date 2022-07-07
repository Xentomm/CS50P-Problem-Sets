from um import count

def main():
    test_count()

def test_count():
    assert count("um") == 1
    assert count("cat") == 0
    assert count("UMMMMMM") == 0
    assert count("Ummmmmmm") == 0

if __name__ == "__name__":
    main()