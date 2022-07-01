import random

def main():
    game()

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 0 < level <= 3:
                break
        except ValueError:
            pass
    return level

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    else:
        raise ValueError
    return x, y

def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except ValueError:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x + y}")
    return False

def game():
    nr_of_rounds = 1
    score = 0
    level = get_level()
    while nr_of_rounds <= 10:
        x, y = generate_integer(level) 
        result = simulate_round(x, y)
        if result == True:
            score += 1
        nr_of_rounds += 1
    print(f"Score: {score}")

if __name__ == "__main__":
    main()