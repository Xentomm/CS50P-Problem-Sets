import sys
import csv

def main():
    check_command_line_arg()
    new_data = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                split_name = row["name"].split(",")
                new_data.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    #print(new_data)

    with open(sys.argv[2], "w", newline = '') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in new_data:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_command_line_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()