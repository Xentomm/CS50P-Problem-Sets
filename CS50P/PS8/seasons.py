from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birthday(birth_date)
        #print(f"{year}, {month}, {day}")
    except:
        sys.exit("Invaild date")
    
    date_of_birth = date(int(year), int(month), int(day))
    todays_date = date.today()

    delta_date = todays_date - date_of_birth
    number_of_minutes = int(delta_date.days) * 24 * 60
    numer_of_minutes_words = p.number_to_words(number_of_minutes, andword="")
    #print(number_of_minutes)
    print(f"{numer_of_minutes_words.capitalize()} minutes")


def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


if __name__ == "__main__":
    main()