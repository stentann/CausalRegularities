from itertools import chain, combinations

def necessaryCheck(conditions, dataSet, predicates, chosenEffect) :
    newMinus = []
    for condition in conditions:
        newList = list(condition)
        copy = newList.copy()
        newList.reverse()
        for conjunct in newList :
            if(len(copy) == 1) :
                newMinus.append(copy)
                break
            copy.remove(conjunct)
            conditionHolds = sufficientCheck(copy, dataSet, predicates, chosenEffect)
            if conditionHolds:
                print("conjunct not necessary")
            if not conditionHolds:
                copy.append(conjunct)
                newMinus.append(copy)
                break

    return newMinus

#tests the given minus condition against all rows of data, returns true if no line violates the condition
def sufficientCheck(condition, data, predicates, chosenEffect):
    effectIndex = 0
    for predicate in predicates:
        if predicate == chosenEffect:
            break
        effectIndex += 1

    for lineNumber in range(len(data)):
        if lineNumber > 0:
            lineElements = data[lineNumber].split()
            #only check rows where effect is false
            if int(lineElements[effectIndex + 1]) == -1:
                #if all inus are met, the minus condition is proven false
                inusMet = 0
                for conjunct in condition:
                    elementNumber = 0
                    for lineElement in lineElements:
                        if elementNumber > 0:
                            #negative inus
                            if list(conjunct)[0] == "~":
                                if list(conjunct)[1] == predicates[elementNumber - 1] and int(lineElement) < 0:
                                    inusMet += 1
                            #positive inus
                            else:
                                if list(conjunct)[0] == predicates[elementNumber - 1] and int(lineElement) > 0:
                                    inusMet += 1
                        elementNumber += 1
                if inusMet == len(condition):
                    return False

    return True

def getDataset(fileName):
    # load data
    dataReader = open(fileName, "r")
    dataSet = {}
    lineCount = 0
    rows = {}
    predicates = []
    for line in dataReader:
        dataSet[lineCount] = line
        if lineCount == 0:
            predicates = line.split()
        else:
            newDict = {}
            newline = line.split()
            elementCounter = 0
            for element in newline:
                if elementCounter != 0:
                    newDict[predicates[elementCounter - 1]] = int(newline[elementCounter])
                elementCounter = elementCounter + 1
            rows[newline[0]] = newDict
        lineCount = lineCount + 1

    return dataSet, predicates, rows

def findAllSubsets(rows, predicates, chosenEffect):
    positive_rows = []
    subsets = set()
    
    for row in rows:
        row = rows.get(row)
        if row.get(chosenEffect) == 1:
            #create set of events in the row, add all of its subsets to the master list
            idx = 0
            rowSet = []
            for predicate in predicates:
                if predicate != chosenEffect:
                    dataItem = ""
                    if row.get(predicate) == -1:
                        dataItem = "~"
                    rowSet.append(dataItem + predicate)
                    idx += 1

            #create all subsets for this row
            rowSubsets = list(chain.from_iterable(combinations(rowSet, r) for r in range(len(rowSet) + 1)))
            for subset in rowSubsets:
                subsets.add(tuple(subset))

    subsets.remove(())
    subsets = sorted(list(subsets), key=len)
    #returns a list of tuples containing all subsets in the dataset that dont contain the chosen effect, and aren't empty
    #the list is in order from smallest to largest subsets
    return subsets

def generateDisjunction(untestedConditions, dataSet, predicates, chosenEffect):
    #for condition in untestedConditions
    #check if it's a superset of proven condition
    #check if it's sufficient
    provenConditions = []

    for condition in untestedConditions:
        passedSupersetCheck = 1
        for provenCondition in provenConditions:
            if set(condition).issuperset(provenCondition):
                passedSupersetCheck = 0
                break
        if passedSupersetCheck:
            if sufficientCheck(condition, dataSet, predicates, chosenEffect):
                provenConditions.append(condition)

    return provenConditions

if __name__ == '__main__':
    # fileName = input("Enter the name of your dataset: ")
    fileName = 'testFile.txt'
    dataSet, predicates, rows = getDataset(fileName)

    print(predicates)
    chosenEffect = input("Enter the desired effect: ")

    untestedConditions = findAllSubsets(rows, predicates, chosenEffect)

    provenConditions = generateDisjunction(untestedConditions, dataSet, predicates, chosenEffect)
    print(f"proven conditions: {provenConditions}")
