# unit test to check creation of valid minus conditions



# ****** ONLY FOR CHOSEN EFFECT Q ******
def minusTest(conditionList){
    
    valid = {{P, R, ~S, ~T, U}, {P, ~R, ~S, ~T, U}, }
    print("valid conditions:")
    for element in valid{
        print(element)    
    }
    
    testPassed = True
    for condition in conditionList{
        if condition not in valid{
             print("invalid condition:")
             print(condition)
             pass = False
        }  
    }
    
    return testPassed    
}


# ****** ONLY FOR CHOSEN EFFECT P ******
def minusTest2(conditionList){
    
    valid = {{~Q, ~R, ~S}, {Q, ~R, S}}
    print("valid conditions:")
    for element in valid{
        print(element)    
    }
    
    testPassed = True
    for condition in conditionList{
        if condition not in valid{
             print("invalid condition")
             print(condition)
             pass = False
        }  
    }
    return testPassed
}


fileName = input("Enter the name of your dataset: ")
result = {}

if fileName == "testFile.txt"{
    result = generateMC(fileName)
    valid = minusTest(result)
    print("Test passed?")
    print(valid)
}

if fileName == "testFile2.txt"{
    result = generateMC(fileName)
    valid = minusTest(result)
    print("Test passed?")
    print(valid)
}




