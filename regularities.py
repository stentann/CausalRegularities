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

# def generateDisjunction(untestedConditions):
#     #for condition in untestedConditions
#         #check if it's a superset of proven condition
#         #check if it's sufficient
#         #check if it's necessary to go through the necessary check
#     provenConditions = {}
#
#     for condition in untestedConditions:
#         passedSupersetCheck = 1
#         for provenCondition in provenConditions:
#             if set(condition).issuperset(provenCondition):
#                 passedSupersetCheck = 0
#                 break
#         if passedSupersetCheck:
#             if sufficientCheck(condition, dataSet, predicates, chosenEffect):
#
#     return provenConditions

def generateDisjunctionWithNecessary(untestedConditions, dataSet, predicates, chosenEffect):
    #for condition in untestedConditions
    #check if it's a superset of proven condition
    #check if it's sufficient
    #check if each conjunct is necessary
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

    provenConditions = necessaryCheck(provenConditions, dataSet, predicates, chosenEffect)

    return provenConditions

if __name__ == '__main__':
    # fileName = input("Enter the name of your dataset: ")
    fileName = 'testFile.txt'
    dataSet, predicates, rows = getDataset(fileName)

    print(predicates)
    chosenEffect = input("Enter the desired effect: ")

    untestedConditions = findAllSubsets(rows, predicates, chosenEffect)
    print(f"untested: {untestedConditions}")

    # provenConditions = generateDisjunction(untestedConditions)
    # print(f"proven (no necessary): {provenConditions}")

    provenConditions = generateDisjunctionWithNecessary(untestedConditions, dataSet, predicates, chosenEffect)
    print(f"proven (no necessary): {provenConditions}")





    minus = []
    for rowVal1, rowData1 in rows.items():
        for rowVal2, rowData2 in rows.items():
            if rowData1[chosenEffect] > 0 and rowData2[chosenEffect] > 0 and rowVal1 != rowVal2:
                matches = set()
                
                # if rowData1[predicate] < 0:
                #     matches.add(('~' + predicate))
                # else:
                #     matches.add(predicate)
                #don't add if a super-set
                valid = True
                minus_temp = minus.copy()
                for conditions in minus_temp:
                    print("matches")
                    print(matches)
                    if matches.issuperset(conditions):
                        valid = False
                        break
                    #checks if previously added elements are supersets
                    if matches.issubset(conditions) :
                        minus.remove(conditions)
                if valid:
                    if sufficientCheck(matches, dataSet, predicates, chosenEffect):
                        minus.append(matches)
    print("Result: ",minus)
#necessaryCheck(minus, dataSet, predicates, chosen_effect)

##### To be removed (all below) #####

#     #cur_val = columns[positive_row[0]][effects[0]]
#     #print(cur_val)
#     #flag = 0
#     matchset = set()
#     for effect in predicates:
#         if effect != chosen_effect:
#             cur_val = rows[positive_row[0]][effect] # set value -1 or 1
#             #matchset = set() #individual matches
#             flag = 0
#             #iterate through a columns row, raise flag if values do not equal
#             for row in positive_row:
#                 rowMatch = set()
#                 if flag == 0:
#                     temp = rows[row][effect]
#                     if temp != cur_val:
#                         flag = 1
#                 #cur_val = temp
#             if flag == 0:
#                 if cur_val > 0:
#                     matchset.add(effect)
#                 else:
#                     matchset.add(('~' + effect))

#         matches = set()
#         for match in matchset:
#             matches.add(match)

#         print("Match: ",matchset)

#         #don't add if a super-set
#         valid = True
#         minus_temp = minus.copy()
#         for conditions in minus_temp:
#             #print(matches)
#             if matches.issuperset(conditions):
#                 valid = False
#                 break
#             #checks if previously added elements are supersets
#             if matches.issubset(conditions) :
#                 minus.remove(conditions)
#         if valid:
#             if basicMinusConditionTest(matches, dataSet, predicates, chosen_effect):
#                 minus.append(matches)