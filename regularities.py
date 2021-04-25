from itertools import chain, combinations
from GetData import GetDataClass

#takes a list of potential minus conditions and returns the same list without any unecessary conjuncts
def necessaryCheck(conditions, dataSet, predicates, chosenEffect) :
    conditions = list(conditions)
    newMinus = []
    for condition in conditions:
        flag = 0
        condition = list(condition)
        if len(condition) == 1 :
             conditionHolds = sufficientCheck(condition, dataSet, predicates, chosenEffect)
             if conditionHolds:
                newMinus.append(condition)
        else :
            minuscond = []
            copy = condition.copy()
            for effect in condition:
                copy.remove(effect)
                conditionHolds = sufficientCheck(copy, dataSet, predicates, chosenEffect)
                if conditionHolds == False:
                    minuscond.append(effect)
                copy.append(effect)
            if minuscond != [] and len(minuscond) != 1:
                newMinus.append(minuscond)
                    
    #remove duplicates
    result = [] 
    for i in newMinus: 
        if i not in result: 
            result.append(i)
    return result


#tests the given minus condition against all rows of data, returns true if no line violates the condition
def sufficientCheck(condition, data, predicates, chosenEffect):
    effectIndex = 0
    for predicate in predicates:
        if predicate == chosenEffect:
            break
        effectIndex += 1

    for lineNumber in range(1,len(data)):
        if lineNumber > 0:
            lineElements = data[lineNumber].split()
            print(lineElements)
            #only check rows where effect is false
            if int(lineElements[effectIndex + 1]) == -1:
                #if all inus are met, the minus condition is proven false
                inusMet = 0
                for conjunct in condition:
                    elementNumber = 0
                    for lineElement in lineElements:
                        if elementNumber > 0:
                            #negative conjunct
                            if list(conjunct)[0] == "~":
                                if list(conjunct)[1] == predicates[elementNumber - 1] and int(lineElement) < 0:
                                    inusMet += 1
                            #positive conjunct
                            else:
                                if list(conjunct)[0] == predicates[elementNumber - 1] and int(lineElement) > 0:
                                    inusMet += 1
                        elementNumber += 1
                if inusMet == len(condition):
                    return False
    return True

#returns a processed text dataset along with a list of predicates and a list of rows
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

#returns a list of all unique subsets (which exclude the chosen effect) from rows where the chosen effect occurred
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
                    if row.get(predicate) != 0:
                        dataItem = ""
                        if row.get(predicate) == -1:
                            dataItem = "~"
                        rowSet.append(dataItem + predicate)
                        idx += 1

            #create all subsets for this row
            rowSubsets = list(chain.from_iterable(combinations(rowSet, r) for r in range(len(rowSet) + 1)))
            for subset in rowSubsets:
                subsets.add(tuple(subset))

    if () in subsets: 
        subsets.remove(())
    subsets = sorted(list(subsets), key=len)
    #returns a list of tuples containing all subsets in the dataset that dont contain the chosen effect, and aren't empty
    #the list is in order from smallest to largest subsets
    return subsets

def generateDisjunctionWithoutSupersets(untestedConditions, dataSet, predicates, chosenEffect):
    #for condition in untestedConditions
    #check if it's a superset of proven condition
    #check if it's sufficient
    provenConditions = []
    for condition in untestedConditions:
        if sufficientCheck(condition, dataSet, predicates, chosenEffect):
            provenConditions.append(condition)

    return provenConditions

def generateDisjunction(untestedConditions, dataSet, predicates, chosenEffect):
    #for condition in untestedConditions
    #check if it's a superset of proven condition
    #check if it's sufficient
    provenConditions = []

    for condition in untestedConditions:
        passedSupersetCheck = 1
        #TODO test replacing this for with necessary code
        for provenCondition in provenConditions:
            if set(condition).issuperset(provenCondition):
                passedSupersetCheck = 0
                break
        if passedSupersetCheck:
            if sufficientCheck(condition, dataSet, predicates, chosenEffect):
                provenConditions.append(condition)

    return provenConditions

if __name__ == '__main__':
    #TODO: accept dataframe format or whah
    # tever format from getData
    
    #fileName = input("Enter the name of your dataset: ")
    fileName = "data/soybean-very-small.data"
    print(f"Using \'{fileName}\'...")
    
    getDataClass = GetDataClass()
    dataSet, predicates, rows = getDataClass.loadAndModifyDataset(fileName)

    print(predicates)
    print(dataSet)
    chosenEffect = input("Enter the desired effect: ")

    untestedConditions = findAllSubsets(rows, predicates, chosenEffect)

    provenConditions = generateDisjunction(untestedConditions, dataSet, predicates, chosenEffect)
    print(f"proven conditions: {provenConditions}")
