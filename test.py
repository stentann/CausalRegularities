import regularities
import sufficientTest
import necessaryTest
import minusGenerationTest
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

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("-test", type=string, help="type of test. Options: all, sufficient, generation"
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

