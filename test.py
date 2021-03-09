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

def necessaryCheckTest():
    #large dataset test
    data, predicates, columns = regularities.getDataset("testfile.txt")

    #choose effect
    chosenEffet = "T"
    #create various testable minus conditions
    minusConditions = [{"~P", "~Q", "R", "~S", "~U"}, {"P", "~Q", "~R", "S", "U"}, {"P", "~Q", "~R", "S", "~U"}]

    test1 = regularities.necessaryCheck(minusConditions[0], data, predicates, chosenEffet)
    test2 = regularities.necessaryCheck(minusConditions[1], data, predicates, chosenEffet)
    test3 = regularities.necessaryCheck(minusConditions[2], data, predicates, chosenEffet)

    passed = True
    test1output = [{"~P"}]
    if(test1 != test1output) :
        print("\nTest1 Failed, output: " , test1)
        passed = False
    test2output = [{"P", "~Q", "~R"}]
    if(test2 != test2output) :
        print("\nTest2 Failed, output: " , test2)
        passed = False
    test3output = [ {"P", "~Q", "~R"}]
    if(test3 != test3output) :
        print("\nTest3 Failed, output: " , test3)
        passed = False

    if(passed == False) :
        return False
    else :
        return True

def parseArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument("-test", type=string, help="type of test. Options: all, necessary, sufficient, generation"
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


