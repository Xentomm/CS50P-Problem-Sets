while True:
    x, y = input("Fraction: ").split("/")
    try:
        new_x = int(x)
        new_y = int(y)
        value = new_x / new_y
        if value <= 1:
            break           
    except (ValueError, ZeroDivisionError):
        pass

new_value = value * 100
if new_value <= 1:
    print("E")
elif new_value >= 99:
    print("F")
else:
    print(f"{int(new_value)}%")
