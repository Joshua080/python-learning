import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False

    if len(s) < 2 or not s[0].isalpha() or not s[1].isalpha():
        return False

    first_digit = False

    for char in s:
        if char.isdigit():
            if not first_digit:
                if char == "0":
                    return False
                first_digit = True
        elif first_digit:
            return False

    for char in s:
        if char in string.punctuation or char == " ":
            return False

    return True

if __name__ == "__main__":
    main()