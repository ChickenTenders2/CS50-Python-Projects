items = {}

while True:
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        for item in sorted(items.keys()):
            print(items[item], item)
        break



