
#load data
#fileName = input("Enter the name of your dataset: ")
fileName = 'testFile.txt'
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
#print(columns)

chosen_effect = input("Enter the desired effect: ")


minus = []
for rowVal1, rowData1 in columns.items():
    for rowVal2, rowData2 in columns.items():
        if rowData1[chosen_effect] == rowData2[chosen_effect] and rowVal1 != rowVal2 and rowData1[chosen_effect] > 0 and  rowData2[chosen_effect] > 0:
            matches = set()
            for effect in effects:
                if rowData1[effect] == rowData2[effect] and effect != chosen_effect:
                    if rowData1[effect] < 0:
                        matches.add(('~' + effect))
                    else:
                        matches.add(effect)
            #don't add if a super-set
            valid = True
            for conditions in minus:
                if matches.issuperset(conditions) :
                    valid = False
                    break
                if matches.issubset(conditions) :
                    minus.remove(conditions)
            if valid == True:
                minus.append(matches)        
                    
                    
print(minus)