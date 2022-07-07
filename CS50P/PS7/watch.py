import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"^<iframe(.)*><\/iframe>$", s):
        if match := re.search(r"(?:http(?:s)*:\/\/(?:www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)", s):
            result = match.groups()
            return f"https://youtu.be/{result[0]}"


if __name__ == "__main__":
    main()