from validator_collection import checkers

def main():
    print(validate(input("Email: ")))

def validate(value):
    try:
        email_address = checkers.is_email(value)
        if email_address:
            return "Valid"
        else:
            return "Invalid"
    except ValueError:
        pass

if __name__ == "__main__":
    main()