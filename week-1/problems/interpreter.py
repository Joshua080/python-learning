math = input("Please enter an arithmitic expression: ")
x = int(math.split(" ")[0])
y = math.split(" ")[1]
z = int(math.split(" ")[2])
def ans(x, y, z):
    match y:
        case "+":
            return float(x+z)
        case "-":
            return float(x-z)
        case "/":
            return float(x/z)
        case "*":
            return float(x*z)
        case _:
            return "Unknown operator"
print(ans(x, y, z))
