def main():
    ans = input("Camel Case: ")
    convert(ans)

def convert(s):
    print("Snake_case: ", end = "")
    for c in s:
        if c.isupper():
            print("_" + c.lower(), end = "")
        else:
            print(c, end = "")
    print()
main()