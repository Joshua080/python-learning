months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
            input_date = input("Please enter a date in middle-edian order: ")

            result = None

            if "/" in input_date:
                result = num_month(input_date)

            elif input_date.split(" ")[0] in months:
                result = word_month(input_date)

            if result is not None:
                 print(result)
                 break

def num_month(date):

    try:
        month = int(date.split("/")[0])
        day = int(date.split("/")[1])
        year = int(date.split("/")[2])
    except ValueError:
         return None
    if day < 1 or day > 31:
         return None
    if month < 1 or month > 12:
         return None

    return f"{year}-{month:02}-{day:02}"

def word_month(date):

    try:

        day = date.split(" ")[1]
        day = int(day[:-1])
        month = int(months.index(date.split(" ")[0])) + 1
        year = int(date.split(" ")[2])

    except ValueError:
         return None

    if day < 1 or day > 31:
         return None

    if month < 1 or month > 12:
         return None

    return f"{year}-{month:02}-{day:02}"

main()