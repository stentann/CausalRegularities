import regularities

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

def main():

    necessaryChecker = necessaryCheckTest()
    if(necessaryChecker == False) :
        print("Necessary Unit Test Failed")
    else :
        print("Necessary Unit Test Passed")

main()
