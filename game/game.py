import sys
import random

while True:
    try:
        size = int(input("Level: "))
        level = random.randint(1, size)
        while True:
            guess = int(input("Guess: "))
            if guess == level:
                print("Just right!")
                sys.exit()
            elif guess < level:
                print("Too small!")
            elif guess > level:
                print("Too large!")
    except ValueError:
        continue

