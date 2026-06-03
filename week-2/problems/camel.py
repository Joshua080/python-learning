def main():
    camel = input("Enter a string in camel case: ")
    print(snake_case(camel))

def snake_case(camel):
    word = ""
    for char in camel:
        if char.islower():
            word += char
        elif char.isupper():
            word += "_" + char.lower()
    return word

main()

    