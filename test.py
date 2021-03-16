import regularities
import argparse

def sufficientCheckUnitTest():
    testPassed = True
    #large dataset test
    data, predicates, rows = regularities.getDataset("testfile.txt")

    #choose effect
    chosenEffet = "Q"
    #create various testable minus conditions
    failingMinusConditions = [{"~P"}, {"P"}, {"~U"}, {"U"}, {"P", "~R"}, {"P", "R", "S", "T", "~U"},
                              {"~P", "R", "S", "~T", "U"}]

    passingMinusConditions = [{"P", "~R", "~S", "~T"}, {"R", "~S", "~T"}, {"P", "R", "~S", "~T", "U"}]

    print("\nTesting \"False\" outputs")
    for minusCondition in failingMinusConditions:
        if regularities.sufficientCheck(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    print("\nTesting \"True\" outputs")
    for minusCondition in passingMinusConditions:
        if not regularities.sufficientCheck(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    return testPassed

def fullAlgorithmTest():
    testPassed = True
    #testFile3.txt test
    data, predicates, rows = regularities.getDataset("testFile3.txt")

    testCases = ["P", "Q", "R", "S", "Z"]

    correctOutputs = {"P": [('~Q', '~R'), ('~Q', '~S'), ('T',), ('~U',)],
        "Q": [('~P', '~S'), ('~S', 'U'), ('~R', '~T'), ('~R', 'U'), ('~P', '~R'), ('~S', '~T')],
        "R": [('S',), ('~Q', 'U'), ('~P', '~Q'), ('~Q', '~T')],
        "S": [('R',), ('~Q', 'U'), ('~Q', '~T'), ('~P', '~Q')],
        "Z": []}

    for effect in testCases:
        untestedConditions = regularities.findAllSubsets(rows, predicates, effect)
        provenConditions = regularities.generateDisjunction(untestedConditions, data, predicates, effect)

        correctOutput = correctOutputs[effect].sort()
        provenConditions = provenConditions.sort()

        if correctOutputs[effect] != provenConditions:
            print(f"Algorithm test failed.")
            print(f"Correct")
        #TODO finish this

def necessaryCheckTest():
    testPassed = True
    #testFile3.txt test
    data, predicates, rows = regularities.getDataset("testFile3.txt")

    testCases = ["P", "Q", "R", "S", "Z"]

    correctOutputs = {"P": [['~Q', '~R'], ['~Q', '~S'], ['T'], ['~U']],
        "Q": [['~P', '~S'], ['~S', 'U'], ['~R', '~T'], ['~R', 'U'], ['~P', '~R'], ['~S', '~T']],
        "R": [['S'], ['~Q', 'U'], ['~P', '~Q'], ['~Q', '~T']],
        "S": [['R'], ['~Q', 'U'], ['~Q', '~T'], ['~P', '~Q']],
        "Z": []}
    for effect in testCases:
        untestedConditions = regularities.findAllSubsets(rows, predicates, effect)
        provenConditions = regularities.generateDisjunctionWithoutSupersets(untestedConditions, data, predicates, effect)
        provenConditions = regularities.necessaryCheck(provenConditions, data, predicates, effect)
        correctOutput = correctOutputs[effect]
        print(correctOutput)
        correctOutput.sort(key=len)
        provenConditions.sort(key=len)
        check =  all(item in correctOutput for item in provenConditions)
        if check == False:
            testPassed = False
            print(f"Algorithm test failed for effect " + effect)
            print("Expected output: ")
            print(correctOutputs[effect])
            print("Output recieved: ")
            print(provenConditions)
        else :
            print(f"Correct Output recieved for effect: " + effect)
    return testPassed

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


def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("-test", help="type of test. Options: all, sufficient, generation"
                                                    " (str) [default: all]", default="all")

    return parser.parse_args()


if __name__ == '__main__':
    args = parseArgs()

    if args.test == 'all':
        print(" ")
        print("Sufficient Unit Test:")
        sufficientPassed = sufficientCheckUnitTest()
        if sufficientPassed:
            print("Sufficient Unit Test Passed")
        else:
            print("Sufficient Unit Test Failed")

        print(" ")
        print(" ")
        print("Necessary Unit Test:")
        necessaryPassed = necessaryCheckTest()
        if necessaryPassed:
            print("Necessary Unit Test Passed")
        else:
            print("Necessary Unit Test Failed")

        print(" ")
        print(" ")
        print("Generation Unit Test:")
        generationPassed = findAllSubsetsCheck()
        if generationPassed:
            print("Generation Unit Test Passed")
        else:
            print("Generation Unit Test Failed")

    elif args.test == 'necessary':
        
        print("Necessary Unit Test:")
        necessaryPassed = necessaryCheckTest()
        if necessaryPassed:
            print("Necessary Unit Test Passed")
        else:
            print("Necessary Unit Test Failed")

    elif args.test == 'sufficient':
        
        print("Sufficient Unit Test:")
        sufficientPassed = sufficientCheckUnitTest()
        if sufficientPassed:
            print("Sufficient Unit Test Passed")
        else:
            print("Sufficient Unit Test Failed")

    elif args.test == 'generation':
        
        print("Generation Unit Test:")
        generationPassed = findAllSubsetsCheck()
        if generationPassed:
            print("Generation Unit Test Passed")
        else:
            print("Generation Unit Test Failed")
