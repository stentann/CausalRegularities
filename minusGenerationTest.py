import regularities
# unit test to check creation of valid minus conditions

def findAllSubsetsCheck():
    testPassed = True
    testPassed2 = False
    passedTests = 0
    #get dataset
    data, predicates, rows = regularities.getDataset("testFile.txt")

    #choose effect
    chosenEffect = "S"

    #create various testable minus conditions
    failingMinusConditions = [{"P", "~Q", "T", "Z"}, {"~P", "~Q", "R", "~T", "U", "~Z"}]

    passingMinusConditions = [{"P", "~Q", "T"}, {"~P", "~Q", "R", "~T", "U"}]

    generatedConditions = regularities.findAllSubsets(rows, predicates, chosenEffect)


    print("\nTesting \"False\" outputs")
    for invalidCondition in failingMinusConditions:
        for generatedCondition in generatedConditions:
            if set(invalidCondition) == set(generatedCondition):
                testPassed = False
                print("{} failed".format(invalidCondition))
    if testPassed == True :
        print("all tests passed")
        
        
    print("\nTesting \"True\" outputs") # this function prints out the sets that passed so we can manually compare to see if any didnt pass (it was much easier this way)
    for validCondition in passingMinusConditions:
        for generatedCondition in generatedConditions:
            if set(validCondition) == set(generatedCondition):
                passedTests += 1
                print("{} passed".format(validCondition))
                
    
    # if all the hard coded valid conditions pass, set variable to true
    if passedTests == len(passingMinusConditions):
        testPassed2 = True
        print("all tests passed")
    else:
        print ("{} test(s) failed.".format(len(passingMinusConditions) - passedTests))

        
    return testPassed & testPassed2 #return & of both boolean values to make sure both invalid AND valid tests passed



passed = findAllSubsetsCheck()

