import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"\b([U|u]m)\b", s)
    return len(matches)

if __name__ == "__main__":
    main()