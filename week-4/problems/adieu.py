names = []
def main():
    while True:
        try:
            current_name = input("Name: ")
            names.append(current_name.title())
        except EOFError:
            print()
            break
    if len(names) == 1:
        one_name(names)
    elif len(names) == 2:
        two_names(names)
    elif len(names) > 2:
        multiple_names(names)

def one_name(name_list):
    print(f"Adieu, adieu, to {name_list[0]}")

def two_names(name_list):
    print(f"Adieu, adieu, to {name_list[0]} and {name_list[1]}")

def multiple_names(name_list):
    size = len(name_list)-1
    print(f"Adieu, adieu, to {", ".join(name_list[:-1])}, and {name_list[size]}")

main()
