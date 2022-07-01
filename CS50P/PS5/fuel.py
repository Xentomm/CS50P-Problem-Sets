def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            new_x = int(x)
            new_y = int(y)
            value = new_x / new_y
            if value <= 1:
                p = int(value * 100)
                return p
            else:
                fraction = input("Fraction: ")       
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{int(percentage)}%"


if __name__ == "__main__":
    main()