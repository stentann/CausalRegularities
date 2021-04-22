import pandas as pd

class GetDataClass:
    def __init__(self):
        pass
 
    def loadAndModifyDataset(self, CSVfilename):
        rawData = pd.read_csv(CSVfilename, header=None)
        cols = list(rawData)
        modifiedData = pd.DataFrame()
        modifiedIndex = 0
        for column in rawData.columns:
            userinput = input(f"What do you want to do with column: \n{rawData[column]}\n(remove/one-hot/custom) : ")
            if (userinput == "remove") : # don't add column to new dataset
                print("Column Removed")
            elif (userinput == "one-hot"): # add one-hot columns to new dataset
                dummies = pd.get_dummies(rawData[column], prefix='onehot')
                print(dummies)
                modifiedData = pd.concat([modifiedData, dummies], axis=1)
                print(len(dummies.columns))
                modifiedIndex = modifiedIndex + len(dummies.columns)
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
        columnNames = list(rawData.columns)
        predicates = rawData.columns
        rawData.rename(columns = {"" : "Idx"}, inplace=True)
        columnNames = rawData.columns
        #put data into formatted dataSet and rows
        for rowIdx, row in rawData.iterrows():
            rowDict = {}
            rowData = rawData.iloc[[rowIdx]]
            dataSetRow = "\t"
            for elementIdx, element in enumerate(rowData):
                if elementIdx != 0:
                    colName = columnNames[elementIdx]
                    print(colName)
                    dataSetRow += str(element) + "\t"
                    print('Test:')
                    print(rowData[colName])
                    print(rowData[colName][rowIdx])
                    rowDict[predicates[elementIdx - 1]] = int(rowData[colName][rowIdx])
            dataSetRow += "\n"
            dataSet[rowIdx] = dataSetRow
            rows[rowIdx] = rowDict
            
        return dataSet, predicates, rows