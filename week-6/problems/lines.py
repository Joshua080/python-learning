import sys
i = 0
if len(sys.argv) == 2:
    if sys.argv[1][-3:] == ".py":
        try:
            with open(sys.argv[1], "r") as file:
                lines = file.readlines()
            for line in lines:
                stripped_line = line.lstrip()
                if not stripped_line.startswith("#") and stripped_line != "":
                    i = i + 1
            print(i)
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("Please enter a python file name")
else:
    sys.exit("Please only enter one command line")