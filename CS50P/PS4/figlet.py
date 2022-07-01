from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) > 1 and (sys.argv[1] == '-f' or sys.argv == '--font'):
    isRandomFont = False
else:
    print("Invalid usage")
    sys.exit(1)

if isRandomFont == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        print("Invalid usage")
        sys.exit(1)
else:
    figlet.setFont(font = random.choice(figlet.getFonts()))

input = input("Input: ")

print("Output: ")
print(figlet.renderText(input))



