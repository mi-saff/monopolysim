import random

def rollDice():
    roll = random.randint(1, 6)
    return roll

counter = 0
while counter < 100:
    result = rollDice()
    print(result)
    counter += 1
