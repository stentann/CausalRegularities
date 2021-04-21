import pandas as pd

class GetDataClass:
    def __init__(self):
        pass
 
    def loadAndModifyDataset(self, CSVfilename):
        rawData = pd.read_csv(CSVfilename)
        cols = list(rawData)
        modifiedData = pd.DataFrame()
        modifiedIndex = 0
        for idx, column in enumerate(cols):
            #print("In for loop")
            userinput = input(f"What do you want to do with column {idx}? (remove/one-hot/custom) : ")
            if (userinput == "remove") : # don't add column to new dataset
                print("Column Removed")
            elif (userinput == "one-hot"): # add one-hot columns to new dataset
                modifiedData[str(modifiedIndex)] = column
                dummies = pd.get_dummies(modifiedData[str(modifiedIndex)], prefix='onehot')
                modifiedData = pd.concat([modifiedData, dummies], axis=1)
                #modifiedData = pd.concat(pd.get_dummies(modifiedData[str(modifiedIndex)], prefix='onehot'), axis=1)
                modifiedIndex+=1
            elif (userinput == "custom"): #prompt user for new column data. Format this data and update dataframe
                newinput = input(f"Please enter new modified column data. Each new value should be seperated by a comma ")
                newinput.strip()
                newdata = newinput.split(",")
                modifiedData[str(modifiedIndex)] = newdata
                modifiedIndex+=1
            else:
                print("Incorrect input. Expected (remove/one-hot/custom)")
        modifiedData.to_csv(f"modified-{CSVfilename}")
        dataSet, predicates, rows = self.loadPreModifiedDataset(f"modified-{CSVfilename}")
        return dataSet, predicates, rows

    #loads dataset we have already modified
    def loadPreModifiedDataset(self, CSVfilename):
        dataSet = {}
        rows = {}
        predicates = []

        rawData = pd.read_csv(CSVfilename)
        predicates = rawData.columns

        #put data into formatted dataSet and rows
        for rowIdx, row in rawData.index:
            rowDict = {}
            rowData = rawData.loc[row, :]
            dataSetRow = "\t"
            for elementIdx, element in enumerate(rowData):
                dataSetRow += str(element) + "\t"
                rowDict[predicates[elementIdx - 1]] = int(rowData[elementIdx])
            dataSetRow += "\n"
            dataSet[rowIdx] = dataSetRow
            rows[rowIdx] = rowDict
            
        return dataSet, predicates, rows