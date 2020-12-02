fileName = input("Enter the name of your dataset: ")
dataSet = open(fileName, "r")
lineCount = 0
columns = {}
for line in dataSet :
    if lineCount == 0 :
        effects = line.split()
    else :
        newDict = {}
        newline = line.split()
        columnArray = []
        elementCounter = 0
        for element in newline :
            if elementCounter != 0 :
                newDict[effects[elementCounter - 1]] = int(newline[elementCounter])
            elementCounter = elementCounter + 1
        columns[newline[0]] = newDict
    lineCount = lineCount + 1
print(effects)        
print(columns)