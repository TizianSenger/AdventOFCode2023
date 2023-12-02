#   Advent of Code 2
contentList = []
productList = []

def readCSVFile():
    with open('data.csv', 'r') as file:
        for row in file:
            tempArr = [] 
            row = row.replace(":", ";")
            row.replace(" ", "")
            tempArr = row.strip().split(";")
            contentList.append(tempArr)
        #print(contentList)

def getProductOfGames():
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
        productList.append(roundMaxGreen * roundMaxBlue * roundMaxRed)
    #print(productList)

def calcSumGames():
    sum = 0
    for number in productList:
        number = int(number)
        sum = sum + number
    print(sum)


readCSVFile()
getProductOfGames()
calcSumGames()