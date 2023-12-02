#   Advent of Code 2
publicGreen = 13
publicRed = 12
publicBlue =14

contentList = []
possibleGames = []

def readCSVFile():
    with open('data.csv', 'r') as file:
        for row in file:
            tempArr = [] 
            row = row.replace(":", ";")
            row.replace(" ", "")
            tempArr = row.strip().split(";")
            contentList.append(tempArr)
        #print(contentList)

def selectPossibleGames():
    for game in contentList:
        roundMaxGreen = 0
        roundMaxRed = 0
        roundMaxBlue = 0
        for round in game:
            tempArr = []
            tempArr = round.split(",")     
            for element in tempArr:
                if "green" in element and int(element.replace("green", "")) > roundMaxGreen:
                    roundMaxGreen = int(element.replace("green", ""))
                if "red" in element and int(element.replace("red", "")) > roundMaxRed:
                    roundMaxRed = int(element.replace("red", ""))
                if "blue" in element and int(element.replace("blue", "")) > roundMaxBlue:
                    roundMaxBlue = int(element.replace("blue", ""))
        if roundMaxGreen <= publicGreen and roundMaxRed <= publicRed and roundMaxBlue <= publicBlue:
            possibleGames.append(game[0])
    #print(possibleGames)

def calcSumGames():
    sum = 0
    for gameNumber in possibleGames:
        gameID = int(gameNumber.replace("Game ", ""))
        sum = sum + gameID
    print(sum)


readCSVFile()
selectPossibleGames()
calcSumGames()