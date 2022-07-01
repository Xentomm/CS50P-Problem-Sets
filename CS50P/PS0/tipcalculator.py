def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    replaced = d.replace("$", "")
    return float(replaced)


def percent_to_float(p):
    replaced = p.replace("%", "")
    return float(replaced) / 100


main()