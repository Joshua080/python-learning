import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def two(s):
    i = 0
    tf = 0
    while i < 2:
        if s[i].isalpha():
            tf += 1
            i += 1
    return tf == 2

def characters(s):
    j = 0
    for char in s:
        j += 1
    if 2 <= j <= 6:
        return True
    else:
        return False

def num(s):
    first_digit = False

    for char in s:
        if char.isdigit():
            if not first_digit:
                if char == "0":
                    return False
                first_digit = True
        elif first_digit:
            return False
    return True

def punctuation(s):
    for char in s:
        if char in string.punctuation or char == " ":
            return False
    return True


def is_valid(s):
    if two(s) and characters(s) and num(s) and punctuation(s):
        return True
    else:
        return False


main()
