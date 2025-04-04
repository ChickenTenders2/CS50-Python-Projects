def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except:
            pass
        else:
            break
    print(gauge(percentage))

def convert(fraction):
    parts = fraction.split("/")
    numerator = int(parts[0])
    denominator = int(parts[1])
    if denominator == 0:
        raise ZeroDivisionError
    elif numerator > denominator:
        raise ValueError
    percentage = round((numerator / denominator) * 100)
    return percentage

def gauge(percentage):
    if percentage == 0:
        return "E"
    elif percentage == 1:
        return "E"
    elif percentage == 99:
        return "F"
    elif percentage == 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{percentage}%"

if __name__ == "__main__":
    main()

