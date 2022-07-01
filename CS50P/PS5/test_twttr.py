import twttr

def main():
    test_shorten_hello()
    test_shorten_twitter()
    test_shorten_numbers()
    test_shorten_punctuation()

def test_shorten_hello():
    assert twttr.shorten("hello") == "hll"

def test_shorten_twitter():
    assert twttr.shorten("twitter") == "twttr"

def test_shorten_numbers():
    assert twttr.shorten("1234") == "1234"

def test_shorten_punctuation():
    assert twttr.shorten("!?$") == "!?$"

if __name__ == "__main__":
    main()