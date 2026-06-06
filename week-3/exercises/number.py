while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("x is not an integer!")
    else:
        break

print(f"You entered: {x}")