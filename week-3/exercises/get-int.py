def main():
    x = get_int("Whats your number? ")
    print(f"You entered: {x}")


def get_int(prompt):
    
    while True:
        
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()