list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input("Date: ")
    try:
        month, day, year = user_input.split("/")
        if (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
            break
    except:
        try:
            old_month, old_day, year = user_input.split(" ")

            month = list.index(old_month) + 1

            day = old_day.replace(",","")

            if (1 <= int(day) <= 31 and 1 <= int(month) <= 12):
                break
        except:
            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")

