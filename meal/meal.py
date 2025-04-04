def main():
    time = input("What time is it? ")
    digital_time = convert(time)
    if 7 <= digital_time <= 8:
        print("breakfast time")
    elif 12 <= digital_time <= 13:
        print("lunch time")
    elif 18 <= digital_time <= 19:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    minutes = float(minute)
    hours = float(hour)
    new_minutes = minutes / 60
    digital_time = hours + new_minutes
    return digital_time

if __name__ == "__main__":
    main()
