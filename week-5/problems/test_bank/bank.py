def main():
    greet = input("Hello, how are you?")
    print(f"${value(greet)}")

def value(greeting):

    if greeting.strip().split()[0].lower() == "hello":
        return 0
    
    elif greeting.strip().lower().startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
