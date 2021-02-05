import regularities

def basicMinusConditionTestUnitTest():
    testPassed = True
    #large dataset test
    data, predicates, columns = regularities.getDataset("testfile.txt")

    #choose effect
    chosenEffet = "Q"
    #create various testable minus conditions
    failingMinusConditions = [{"~P"}, {"P"}, {"~U"}, {"U"}, {"P", "~R"}, {"P", "R", "S", "~T", "U"},
                              {"~P", "R", "~S", "T", "~U"}]

    passingMinusConditions = [{"P", "~R", "~S", "~T"}, {"R", "~S", "~T"}, {"P", "R", "~S", "~T", "U"}]

    print("\nIncorrect minus condition test:")
    for minusCondition in failingMinusConditions:
        if regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    print("\nCorrect minus condition test:")
    for minusCondition in passingMinusConditions:
        if not regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    return testPassed

def main():

    basicMinusConditionTestUnitTestPassed = basicMinusConditionTestUnitTest()
    print("\nbasicMinusConditionTestUnitTest\npassed: ", basicMinusConditionTestUnitTestPassed)

main()