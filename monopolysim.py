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

def createChance():
    chance_cards = ["Advance to Go", "Advance to Illinois Ave", "Advance to St. Charles Place", "Advance token to nearest utility", "Advance token to nearest railroad", "Bank pays you $50", "Get out of Jail Free", "Go back 3 spaces", "Go to Jail", "Make general repairs", "Pay $15 fine", "Take a trip to Reading Railroad", "Take a walk on the Boardwalk", "You have been elected Chairman", "Your building and loan matures", "You have won crossword"]
    random.shuffle(chance_cards)
    #print chance_cards
    return chance_cards

def createCommunity():
    community_chest_cards = ["Advance to Go", "Bank error in your favor", "Doctor's fees", "From sale of stock you get $50", "Get out of Jail Free", "Go to Jail", "Grand Opera Night", "Holiday fund matures", "Income tax refund", "It is your birthday", "Life insurance matures", "Pay hospital fees of $100", "Pay school fees of $150", "Receive $25 consultancy fee", "You are assessed for street repairs", "You have won second prize in a beauty contest", "You inherit $100"]
    random.shuffle(community_chest_cards)
    return community_chest_cards

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

def chanceCard(chance_card, currentPos):
    if chance_card == "Advance to Go":
        return 0

    elif chance_card == "Advance to Illinois Ave":
        return 24

    elif chance_card == "Advance to St. Charles Place":
        return 11

    elif chance_card == "Advance token to nearest utility":
        if currentPos > 12 and currentPos <= 28:
            return 28
        else:
            return 12

    elif chance_card == "Advance token to nearest railroad":
        if currentPos > 35 or currentPos <= 5:
            return 5
        elif currentPos > 5 and currentPos <= 15:
            return 15
        elif currentPos > 15 and currentPos <= 25:
            return 25
        elif currentPos > 25 and currentPos <= 35:
            return 35

    elif chance_card == "Go back 3 spaces":
        if currentPos < 3:
            return currentPos + 40 - 3
        else:
            return currentPos - 3

    elif chance_card == "Go to jail":
        return 10

    elif chance_card == "Take a trip to Reading Railroad":
        return 5

    elif chance_card == "Take a walk on the Boardwalk":
        return 39

    else:
        return currentPos

def communityCard(community_chest, currentPos):
    if community_chest == "Go to Jail":
        return 10

    elif community_chest == "Advance to Go":
        return 0

    else:
        return currentPos

myboard = createBoard()
chance_cards = createChance()
community_chest_cards = createCommunity()
dict([])
while counter < 1000000:
    #print "Current position: ", myboard[currentPos][0]
    diceRoll = rollDice()
    #print "Rolled a ",diceRoll
    newPos = currentPos + diceRoll
    if newPos >= 40:
        newPos = newPos - 40
    elif myboard[newPos][0] == "Chance":
        chance_card = chance_cards.pop(0)
        #print "Chance! ", chance_card
        tempPos = chanceCard(chance_card, newPos)
        if tempPos != newPos:
            myboard[newPos][1] += 1
            #print "Moved from", myboard[newPos][0], "to", myboard[tempPos][0]
            newPos = tempPos
        chance_cards.append(chance_card)
        #print chance_cards
    elif myboard[newPos][0] == "Community Chest":
        community_chest = community_chest_cards.pop(0)
        tempPos = communityCard(community_chest, newPos)
        if tempPos != newPos:
            myboard[newPos][1] += 1
            newPos = tempPos
        community_chest_cards.append(community_chest)

    elif myboard[newPos][0] == "Go To Jail":
        myboard[newPos][1] += 1
        newPos = 10
        counter += 1
        #print "Go to jail!"

    currentPos = newPos
    #print "New position: ", myboard[newPos][0]

    myboard[currentPos][1] += 1
    counter += 1
printBoard(myboard, counter)
