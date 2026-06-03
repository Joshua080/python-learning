due = 50
paid = 0
while due > 0:
    print("Amount Due:", due)
    amount = input("Insert Coin: ")
    if amount in ["25", "10", "5"]:
        due -= int(amount)
        paid += int(amount)
change = paid - 50
print("Change Owed:", change)
