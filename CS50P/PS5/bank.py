import re

def main():
    user_input = input().lower()
    greeting = re.split(',| ', user_input)
    print(value(greeting[0]))


def value(greeting):
    if (greeting == "hello"):
        return "$0"
    elif(greeting[0] == "h"):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()