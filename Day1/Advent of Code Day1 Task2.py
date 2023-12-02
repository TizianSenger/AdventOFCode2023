#   Advent of Code 1
listOfStringNumbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

contentList = []
numberList = []
newlist = []

def readCSVFile():
    with open('data.csv', 'r') as file:
        for row in file:
            contentList.append(row.strip())
        #print(contentList)
def stringSlice():
    tempElement = ""
    status = False
    for element in contentList:
        for number in listOfStringNumbers:
            if number in element:
                status = True
                if tempElement == "":
                    tempElement = (element.replace(number[:-1], str(listOfStringNumbers.index(number) + 1)))
                    print("original:    " + element)
                    print("bearbeitet:  " + tempElement + "  geändert: " + number)
                else:
                    tempElement = (tempElement.replace(number[:-1], str(listOfStringNumbers.index(number) + 1)))
                    print("bearbeitet:  " + tempElement + "  geändert: " + number)
        print("")
        
        if status == True:
            newlist.append(tempElement)
            tempElement = ""
            status = False   
        else:
            newlist.append(element)
            status = False

    firstNumber = ""
    secondNumber = ""
    for element in newlist:
        #print(element)
        for digit in element:
            if digit.isdigit():
                firstNumber = digit
                break
        for digit in element[::-1]:
            if digit.isdigit():
                secondNumber = digit
                break
        #print(firstNumber + secondNumber)
        numberList.append(firstNumber + secondNumber)


def calcNumbers():
    sum = 0
    for digit in numberList:
        sum = sum + int(digit)
    print(sum)
    print("real: 54578")
    #print("asdfasdfasdfasdfasdf".replace("a", "!"))

readCSVFile()
stringSlice()
calcNumbers()
