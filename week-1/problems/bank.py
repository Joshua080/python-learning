greet = input("Hello, how are you?")
if greet.strip().lower().startswith("h"):
    print("$20")
elif greet.strip().lower().split()[0] == "hello":
    print("$0")
else:
    print("$100")