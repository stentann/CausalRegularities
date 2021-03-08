import regularities

def sufficientCheckUnitTest():
    testPassed = True
    #large dataset test
    data, predicates, columns = regularities.getDataset("testfile.txt")

    print(f"predicates: {predicates}")
    print(f"cols: {columns}")
    print(f"data: {data}")

    #choose effect
    chosenEffet = "Q"
    #create various testable minus conditions
    failingMinusConditions = [{"~P"}, {"P"}, {"~U"}, {"U"}, {"P", "~R"}, {"P", "R", "S", "T", "~U"},
                              {"~P", "R", "S", "~T", "U"}]

    passingMinusConditions = [{"P", "~R", "~S", "~T"}, {"R", "~S", "~T"}, {"P", "R", "~S", "~T", "U"}]

    print("\nTesting \"False\" outputs")
    for minusCondition in failingMinusConditions:
        if regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    print("\nTesting \"True\" outputs")
    for minusCondition in passingMinusConditions:
        if not regularities.basicMinusConditionTest(minusCondition, data, predicates, chosenEffet):
            testPassed = False
            print("{} failed".format(minusCondition))
    return testPassed

if __name__ =='__main__':
    sufficientCheckUnitTestPassed = sufficientCheckUnitTest()
    print("\nsufficientCheckUnitTest\npassed: ", sufficientCheckUnitTestPassed)
