def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    word_without_vowels = ""
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u'] :
            word_without_vowels += letter
    return word_without_vowels

if __name__ == "__main__":
    main()