import regularities

def basicMinusConditionTestUnitTest():
    testPassed = True
    #large dataset test
    data, predicates = regularities.getDataset("testfile.txt")

    #choose effect
    chosenEffet = "Q"
    #create various testable minus conditions
    failingMinusConditions = [{"~P"}, {"P"}, {"~U"}, {"U"}, {"P", "~R"}, {"P", "R", "S", "~T", "U"},
                              {"~P", "R", "~S", "T", "~U"}]

    passingMinusConditions = [{"P", "~R", "~S", "~T"}, {"R", "~S", "~T"}, {"P", "R", "~S", "~T", "U"}]

    for minusCondition in failingMinusConditions:
        if regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("%s failed", minusCondition)
    for minusCondition in passingMinusConditions:
        if not regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("%s failed", minusCondition)
    return testPassed

def main():

    basicMinusConditionTestUnitTestPassed = basicMinusConditionTestUnitTest()
    print("basicMinusConditionTestUnitTest\npassed: ", basicMinusConditionTestUnitTestPassed)

main()