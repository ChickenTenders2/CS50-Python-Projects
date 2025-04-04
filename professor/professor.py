import random

def main():

    questions = 10
    score = 0
    level = get_level()

    while questions > 0:
        try:
            values = generate_integer(level)
            x, y = values
            answer = x + y
            attempts = 0

            while True:
                response = int(input(f"{x} + {y} = "))
                if response == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
                    if attempts == 3:
                        print(f"{x} + {y} = {answer}")
                        break
            questions -= 1

        except ValueError:
            continue

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise ValueError()
            else:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y

if __name__ == "__main__":
    main()
