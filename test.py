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
    

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("-test", help="type of test. Options: all, sufficient, generation"
                                                    " (str) [default: all]", default="all")

    return parser.parse_args()

if __name__ == '__main__':
    args = parseArgs()

    if args.test == 'all':
        sufficientPassed = sufficientCheckUnitTest()
        if sufficientPassed:
            print("Sufficient Unit Test Passed")
        else:
            print("Sufficient Unit Test Failed")

        necessaryPassed = necessaryCheckTest()
        if necessaryPassed:
            print("Necessary Unit Test Passed")
        else:
            print("Necessary Unit Test Failed")

        print("Generation test not implemented")

    elif args.test == 'necessary':
        necessaryPassed = necessaryCheckTest()
        if necessaryPassed:
            print("Necessary Unit Test Passed")
        else:
            print("Necessary Unit Test Failed")

    elif args.test == 'sufficient':
        sufficientPassed = sufficientCheckUnitTest()
        if sufficientPassed:
            print("Sufficient Unit Test Passed")
        else:
            print("Sufficient Unit Test Failed")

    elif args.test == 'generation':
        print("Generation test not implemented")

