fruits = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "sweet cherries": "100"
}

user_input = input("Item: ").lower()

if user_input in fruits:
    print("Calories:", fruits[user_input])
else:
    exit()

