#   Advent of Code 3
contentList = []

def readCSVFile():
    with open('data.csv', 'r') as file:
        for row in file:
            contentList.append(row.strip())

readCSVFile()
