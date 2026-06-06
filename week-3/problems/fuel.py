while True:

    fuel = input("How much fuel do you have left? PLease enter as a fraction 'x/y': ")

    try:
        x = int(fuel.split("/")[0])
        y = int(fuel.split("/")[1])
    except (ValueError, IndexError):
        print("Please enter correct integer values in the correct format")
        continue

    if x > y:
        continue
    if x < 0:
        continue
    try:
        percent = round(x/y*100)
    except ZeroDivisionError:
        print("You cant have 0 as the second value")
        continue
    break
if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")