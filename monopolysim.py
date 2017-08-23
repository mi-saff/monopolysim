import random

def createBoard():
   board = [["Go", 0]]
   board.append(["Mediterranean Avenue", 0])
   board.append(["Community Chest", 0])
   board.append(["Baltic Avenue", 0])
   board.append(["Income Tax", 0])
   board.append(["Reading Railroad", 0])
   board.append(["Oriental Avenue", 0])
   board.append(["Chance", 0])
   board.append(["Vermont Avenue", 0])
   board.append(["Connecticut Avenue", 0])
   board.append(["Jail", 0])
   board.append(["St. Charles Place", 0])
   board.append(["Electric Company", 0])
   board.append(["States Avenue", 0])
   board.append(["Virginia Avenue", 0])
   board.append(["Pennsylvania Railroad", 0])
   board.append(["St. James Place", 0])
   board.append(["Community Chest", 0])
   board.append(["Tennessee Avenue", 0])
   board.append(["New York Avenue", 0])
   board.append(["Free Parking", 0])
   board.append(["Kentucky Avenue", 0])
   board.append(["Chance", 0])
   board.append(["Indiana Avenue", 0])
   board.append(["Illinois Avenue", 0])
   board.append(["B & O Railroad", 0])
   board.append(["Atlantic Avenue", 0])
   board.append(["Vetnor Avenue", 0])
   board.append(["Water Works", 0])
   board.append(["Marvin Gardens", 0])
   board.append(["Go To Jail", 0])
   board.append(["Pacific Avenue", 0])
   board.append(["North Carolina Avenue", 0])
   board.append(["Community Chest", 0])
   board.append(["Pennsylvania Avenue", 0])
   board.append(["Short Line", 0])
   board.append(["Chance", 0])
   board.append(["Park Place", 0])
   board.append(["Luxury Tax", 0])
   board.append(["Boardwalk", 0])
   return board

def rollDice():
    roll = random.randint(1, 6) + random.randint(1, 6)
    return roll

counter = 0.0
currentPos = 0
newPos = 0

def printBoard(board, numrolls):
    from operator import itemgetter
    board = sorted(board, key=itemgetter(1), reverse=True)
    for item in board:
        print item[0], "occurs", item[1], "times with a probability of", item[1]/numrolls * 100

myboard = createBoard()
dict([])
while counter < 1000000:
    #print "Current position: ", currentPos
    diceRoll = rollDice()
    #print "Rolled a ",diceRoll
    newPos = currentPos + diceRoll
    if newPos >= 40:
        newPos = newPos - 40
    elif myboard[newPos][0] == "Go To Jail":
        myboard[newPos][1] += 1
        newPos == 10
        counter += 1

    currentPos = newPos
    #print "New position: ", newPos

    myboard[currentPos][1] += 1
    counter += 1
printBoard(myboard, counter)
