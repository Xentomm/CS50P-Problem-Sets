import re
def main():
    time = input("What time is it? ")
    new_time_small = time.split(':')
    new_time = re.split(':| ', time)

    if len(new_time) > 2:
        meal_time = convert(new_time)
        if new_time[2] == "p.m.":
            meal_time += 12.0
    else:
        meal_time = convert(new_time_small)

    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time") 
    else:
        return 0

def convert(time):
    meal_time = float(time[0]) + float(time[1])/60
    return meal_time


if __name__ == "__main__":
    main()