import inflect

p = inflect.engine()

names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")