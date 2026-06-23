import random
import statistics

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
for card in cards:
    print(card)
    
    
marks = [90, 80, 85, 70, 95]    
print(statistics.mean(marks))