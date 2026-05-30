x = input("What is your first number?")
y = input("What is your second number?")
operator = input("What operator do you want to use?")
if operator == "+":
    print(round(float(x) + float(y)))
elif operator == "-":
    print(round(float(x) - float(y)))
elif operator == "*":
    print(round(float(x) * float(y)))
elif operator == "/":
    print(round(float(x) / float(y)))
else:    print("Invalid operator")