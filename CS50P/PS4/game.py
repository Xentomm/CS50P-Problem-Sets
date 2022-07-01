import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess >= 1:
            break
    except ValueError:
        pass

if guess < 1:
    pass
elif guess < number:
    print("Too small!")
elif guess > number:
    print("Too large!")
else:
    print("Just right!")