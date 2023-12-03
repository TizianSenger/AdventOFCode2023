#   Advent of Code 3

contentList = []

def readCSVFile():
    with open('D:\CodeOfAdvent2023 Repo\AdventOFCode2023\Day3\data.csv', 'r') as file:
        for row in file:
            contentList.append(row.strip())
            

readCSVFile()
