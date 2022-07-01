def main():
    x, y, z = input("Expression: ").split(sep = ' ')
    print(calculate(x,y,z))

def calculate(x, znak, z):
    if znak == '+':
        return float(x) + float(z)
    elif znak == '-':
        return float(x) - float(z)
    elif znak == '*':
        return float(x) * float(z)
    elif znak == '/' and float(z) != 0:
            return float(x) / float(z)
    else:
        return False

main()