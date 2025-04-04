while True:
    try:
        response = input("Fraction: ").split("/")
        numerator = int(response[0])
        denominator = int(response[1])
        fraction = round((numerator / denominator) * 100)
        if fraction > 100:
            continue
    except (ValueError, IndexError, ZeroDivisionError):
        pass
    else:
        if fraction == 0:
            print("E")
        elif fraction == 1:
            print("E")
        elif fraction == 99:
            print("F")
        elif fraction == 100:
            print("F")
        elif 1 < fraction < 99:
            print(f"{fraction}%")
        break
