#tests the given minus condition against all rows of data, returns true if no line violates the condition
def basicMinusConditionTest(condition, data, predicates, thisEffect):
    effectIndex = 0
    for predicate in predicates:
        if predicate == thisEffect:
            break
        effectIndex += 1

    for lineNumber in range(len(data)):
        if lineNumber > 0:
            lineElements = data[lineNumber].split()
            #only check rows where effect is false
            if int(lineElements[effectIndex + 1]) == -1:
                #if all inus are met, the minus condition is proven false
                inusMet = 0
                #print("Condition:")
                #print(condition)
                for inus in condition:
                    elementNumber = 0
                    for lineElement in lineElements:
                        if elementNumber > 0:
                            #negative inus
                            if list(inus)[0] == "~":
                                if list(inus)[1] == predicates[elementNumber - 1] and int(lineElement) < 0:
                                    inusMet += 1
                            #positive inus
                            else:
                                if list(inus)[0] == predicates[elementNumber - 1] and int(lineElement) > 0:
                                    inusMet += 1
                        elementNumber += 1
                if inusMet == len(condition):
                    return False

    return True

def necessaryCheck(minus, data, predicates, chosen) :
    newMinus = []
    for condition in minus:
        newList = list(condition)
        copy = set(newList.copy())
        newList.reverse()
        for effect in newList :
            if(len(copy) == 1) :
                newMinus.append(copy)
                break
            copy.remove(effect)
            if(copy == {'~'}) :
                break
            print("copy")
            print(copy)
            conditionHolds = basicMinusConditionTest(copy, data, predicates, chosen)
            if conditionHolds == False:
                copy.add(effect)
                newMinus.append(copy)
                break
    return newMinus

def getDataset(fileName):
    # load data
    dataReader = open(fileName, "r")
    dataSet = {}
    lineCount = 0
    columns = {}
    effects = []
    for line in dataReader:
        dataSet[lineCount] = line
        if lineCount == 0:
            effects = line.split()
        else:
            newDict = {}
            newline = line.split()
            elementCounter = 0
            for element in newline:
                if elementCounter != 0:
                    newDict[effects[elementCounter - 1]] = int(newline[elementCounter])
                elementCounter = elementCounter + 1
            columns[newline[0]] = newDict
        lineCount = lineCount + 1

    return dataSet, effects, columns


chosen_effect = input("Enter the desired effect: ")
fileName = 'testFile.txt'
dataSet, effects, columns = getDataset(fileName)

minus = []
for rowVal1, rowData1 in columns.items():
    for rowVal2, rowData2 in columns.items():
        if rowData1[chosen_effect] == rowData2[chosen_effect] and rowVal1 != rowVal2 and rowData1[chosen_effect] > 0 and rowData2[chosen_effect] > 0:
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
                #checks if previously added elements are supersets
                if matches.issubset(conditions) :
                    minus.remove(conditions)
            if valid:
                if basicMinusConditionTest(matches, dataSet, effects, chosen_effect):
                    minus.append(matches)

necessaryCheck(minus, dataSet, effects, chosen_effect)
