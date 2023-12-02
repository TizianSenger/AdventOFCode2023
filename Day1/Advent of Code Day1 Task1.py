#   Advent of Code 1
contentList = []
numberList = []

def readCSVFile():
    with open('data.csv', 'r') as file:
        for row in file:
            contentList.append(row.strip())
        #print(contentList)

def stringSlice():
    firstNumber = ""
    secondNumber = ""
    for element in contentList:
        for digit in element:
            if digit.isdigit():
                firstNumber = digit
                break
        for digit in element[::-1]:
            if digit.isdigit():
                secondNumber = digit
                break
        numberList.append(firstNumber + secondNumber)

def calcNumbers():
    sum = 0
    for digit in numberList:
        sum = sum + int(digit)
    print(sum)

readCSVFile()
stringSlice()
calcNumbers()