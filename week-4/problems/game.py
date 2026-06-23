import random
import sys

while True:

    try:
        n = int(input("Level: "))
        if n < 0:
            continue
        else:
            break
    except ValueError:
        continue

rand_num = random.randint(1, n)

while True:

    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess == rand_num:
                sys.exit("Just right!")
            elif guess < rand_num:
                print("Too small!")
                continue
            elif guess > rand_num:
                print("Too large!")
                continue

        else:
            continue
    except ValueError:
        continue
