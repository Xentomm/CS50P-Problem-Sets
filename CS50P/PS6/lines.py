import sys

def main():
    check_command_line_arg()
    try:
        f = open(sys.argv[1], "r")
        lines = f.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")
    
    counter = 0
    for line in lines:
        if check_comment_or_empty_line(line) == False:
            counter += 1
    print(f"Number of lines: {counter}")

def check_command_line_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    
def check_comment_or_empty_line(line):
    if line.isspace():
        return True
    if line.lstrip().startswith("#"):
        return True
    else:
        return False

if __name__ == "__main__":
    main()

