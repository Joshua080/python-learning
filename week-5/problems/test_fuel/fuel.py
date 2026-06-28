def main():
    while True:
        try:
            fuel = input("Fraction: ")
            print(gauge(convert(fuel)))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    try:
        x = int(fraction.split("/")[0])
        y = int(fraction.split("/")[1])
    except (ValueError, IndexError):
        raise
    if y == 0:
        raise ZeroDivisionError

    if not (0 <= x <= y):
        raise ValueError

    try:
        percent = round(x/y*100)
    except ZeroDivisionError:
        raise
    return percent


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
