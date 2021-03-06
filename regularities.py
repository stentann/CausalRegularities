from itertools import chain, combinations

def necessaryCheck(minus, data, predicates, chosen) :
    newMinus = []
    for condition in minus:
        newList = list(condition)
        copy = newList.copy()
        newList.reverse()
        for effect in newList :
            if(len(copy) == 1) :
                newMinus.append(copy)
                break
            copy.remove(effect)
            conditionHolds = basicMinusConditionTest(copy, data, predicates, chosen)
            if conditionHolds == False:
                copy.append(effect)
                newMinus.append(copy)
                break
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
    print(predicates)
    # print(columns)

    return dataSet, predicates, rows
    
def find_all_subsets(rows, chosenEffect):
    positive_rows = []
    subsets = []
    
    for row in rows:
        if row[chosen_effect] == 1:
            s = list(row)
            rowSubsets = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
            subsets.append(rowSubsets)
    
    return subsets
       

if __name__ == '__main__':
    # fileName = input("Enter the name of your dataset: ")
    fileName = 'testFile.txt'
    dataSet, predicates, rows = getDataset(fileName)

    #TODO: turn dataset into "~P, Q, ~R" format and fix find_all_subsets to remove subsets w/ effect and duplicates

    chosen_effect = input("Enter the desired effect: ")
    print("rows")
    for row in rows:
        print(rows.get(row))
    untestedConditions = find_all_subsets(rows, chosen_effect)

    minus = []
    for rowVal1, rowData1 in rows.items():
        for rowVal2, rowData2 in rows.items():
            if rowData1[chosen_effect] > 0 and rowData2[chosen_effect] > 0 and rowVal1 != rowVal2:
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
                    if basicMinusConditionTest(matches, dataSet, predicates, chosen_effect):
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