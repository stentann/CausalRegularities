import pandas as pd
import sys

class GetDataClass:
    def __init__(self):
        pass
 
    def loadAndModifyDataset(self, CSVfilename):
        rawData = pd.read_csv(CSVfilename, header=None)
        cols = list(rawData)
        modifiedData = pd.DataFrame()
        modifiedIndex = 0
        colCounter = 1
        for column in rawData.columns:
            correctInput = False
            while not correctInput :
                columnName = input(f"\nName for column " + str(colCounter) + ": ")
                userinput = input(f"What do you want to do with column: {columnName} (keep/remove/one-hot/custom) : ")
                if (userinput == "remove") : # don't add column to new dataset
                    print("Column Removed")
                    correctInput = True
                elif (userinput == "one-hot"): # add one-hot columns to new dataset
                    dummies = pd.get_dummies(rawData[column], prefix=columnName)
                    modifiedData = pd.concat([modifiedData, dummies], axis=1)
                    modifiedIndex = modifiedIndex + len(dummies.columns)
                    correctInput = True
                elif (userinput == "custom"): #prompt user for new column data. Format this data and update dataframe
                    newinput = input(f"Please enter new modified column data. Each new value should be seperated by a comma ")
                    newinput.strip()
                    newdata = newinput.split(",")
                    modifiedData[columnName] = newdata
                    modifiedIndex+=1
                    correctInput = True
                elif (userinput == "keep"): #add column 'as is' to dataframe
                    modifiedData[columnName] = rawData[column]
                    modifiedIndex+=1
                    correctInput = True
                else:
                    print("\nIncorrect input. Expected (remove/one-hot/custom/keep)")
                    print("Try again:")
            colCounter+=1
        modifiedData.replace(to_replace=0, value="-1", inplace=True)
        modifiedData.replace(to_replace='0', value=-1, inplace=True)
        modifiedData.replace(to_replace='?', value=0, inplace=True)
        modifiedData = modifiedData.apply(pd.to_numeric)
        print("\nModified Dataset:")
        print(modifiedData)
        modifiedData.to_csv(f"modified-{CSVfilename}")
        print(f"\nModified dataset saved to modified-{CSVfilename}\n")
        dataSet, predicates, rows = self.loadPreModifiedDataset(f"modified-{CSVfilename}")

        return dataSet, predicates, rows

    #loads dataset we have already modified
    def loadPreModifiedDataset(self, CSVfilename):
        dataSet = {}
        rows = {}
        predicates = []

        rawData = pd.read_csv(CSVfilename)
        rawData = rawData.apply(pd.to_numeric)
        columnNames = list(rawData.columns)
        predicates = columnNames[1:]
        columnNames = rawData.columns
        #put data into formatted dataSet and rows
        for rowIdx, row in rawData.iterrows():
            rowDict = {}
            rowData = rawData.iloc[rowIdx, :]
            dataSetRow = "\t"
            for elementIdx, element in enumerate(rowData):
                if elementIdx != 0:
                    if rowIdx != 0 and element != -1 and element != 0 and element != 1:
                        sys.exit(f"Error loading modified dataset in column {elementIdx}, row {rowIdx} \
                        \nExpected -1, 0, or 1. Found {element} which is type {type(element)}\n")
                    colName = columnNames[elementIdx]
                    dataSetRow += str(element) + "\t"
                    rowDict[predicates[elementIdx - 1]] = int(rowData[elementIdx])
            dataSetRow += "\n"
            dataSet[rowIdx] = dataSetRow
            rows[rowIdx] = rowDict
            
        return dataSet, predicates, rows