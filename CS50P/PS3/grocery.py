d = {}

while True:
    try:
        item = input()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        for key in sorted(d.keys()):
            print(d[key], key.upper())
        break
