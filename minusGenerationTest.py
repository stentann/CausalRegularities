import regularities
# unit test to check creation of valid minus conditions

def findAllSubsetsCheck():
    testPassed = True
    #get dataset
    data, predicates, rows = regularities.getDataset("testfile.txt")

    #choose effect
    chosenEffect = "S"

    #create various testable minus conditions
    failingMinusConditions = [{"P", "~Q", "T", "Z"}, {"~P", "~Q", "R", "~T", "U", "~Z"}]

    passingMinusConditions = [{"P", "~Q", "T"}, {"~P", "~Q", "R", "~T", "U"}]

    generatedConditions = regularities.findAllSubsets(rows, predicates, chosenEffect)

    #print("generatedConditions: ")
    #print(generatedConditions)

    print("\nTesting \"False\" outputs")
    for minusCondition in failingMinusConditions:
        if minusCondition.issubset(generatedConditions):
            testPassed = False
            print("{} failed".format(minusCondition))
    print("\nTesting \"True\" outputs")
    for minusCondition in passingMinusConditions:
        if not minusCondition.issubset(generatedConditions):
            testPassed = False
            print("{} failed".format(minusCondition))
    return testPassed

passed = findAllSubsetsCheck()