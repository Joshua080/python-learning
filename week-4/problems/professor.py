import random

def main():
    n = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(n)
        y = generate_integer(n)
        z = x + y
        mistakes = 0

        while mistakes < 3:
            try:
                math_ans = int(input(f"{x} + {y} = "))
                if math_ans == z:
                    score += 1
                    break
                else:
                    print("EEE")
                    mistakes += 1
            except ValueError:
                    print("EEE")
                    mistakes += 1
        if mistakes == 3:
            print(f"{x} + {y} = {z}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl not in [1, 2, 3]:
                continue
            else:
                return lvl
        except ValueError:
            continue


def generate_integer(level):
    match level:
        case 1:
            min = 0
            max = 9
        case 2:
            min = 10
            max = 99
        case 3:
            min = 100
            max = 999

    return random.randint(min, max)


if __name__ == "__main__":
    main()
