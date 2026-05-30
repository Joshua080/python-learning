def main():
    name = input("What is your name? ")
    hello(name)
    number = int(input("Enter a number: "))
    print("The square of ", number, " is ", square(number))

def hello(to = "world"):
    print("Hello, ", to)
    
def square(x):
    return x * x
    
main()
