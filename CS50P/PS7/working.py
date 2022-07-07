import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    isCorrectFormat = re.search("^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if isCorrectFormat:
        matches = isCorrectFormat.groups()
        if int(matches[1]) > 12 or int(matches[5]) > 12:
            raise ValueError
        first_time = formatting(matches[1], matches[2], matches[3])
        second_time = formatting(matches[5], matches[6], matches[7])
        return f"{first_time} to {second_time}"
    else:
        raise ValueError

def formatting(hour, minute, am_pm):
    if am_pm == 'PM':
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minute == None:
        new_minute = ':00'
        new_time = f"{new_hour:02}" + new_minute
    else:
        new_time = f"{new_hour:02}" + ":" + minute
    return new_time

if __name__ == "__main__":
    main()