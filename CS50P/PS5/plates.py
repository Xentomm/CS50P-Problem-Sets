def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum() and not s[0:2].isdigit() and zeros(s) and letters_after_digit(s):
        return True
    else:
        return False

def zeros(s):
    for character in s:
        if character.isalpha() == False:
            if character == '0':
                return False
            else:
                return True

def letters_after_digit(s):
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            else:
                return True


if __name__ == "__main__":
    main()