import pandas as pd

class GetData:
    def loadCSVDataset(self, fileName):
        rawdata = pd.read_csv(fileName)
        return rawdata
        
    def modifyDataset(self, rawdata):
        cols = list(rawdata)
        modifiedData = pd.DataFrame() # to be filled with desired data
        
        for idx, column in iterate(cols):
            input = input(f"What do you want to do with column {idx}? (remove/one-hot/custom) : ")
            if (input == "remove") : # don't add column to new dataset
                print("Column Removed")
            elif (input == "one-hot"): # add one-hot columns to new dataset
                modifiedData[f'{idx}'] = column
                modifiedData = pd.concat(pd.get_dummies(modifiedData[f'{idx}'], prefix='onehot'), axis=1)
            elif (input == "custom"): #prompt user for new column data. Format this data and update dataframe
                input = input(f"Please enter new modified column data. Each new value should be seperated by a comma ")
                input.strip()
                newdata = input.split(",")
                
            else:
                print("Incorrect input. Expected (remove/one-hot/custom)")
        return 
        
    #loads dataset we have already modified
    def loadPreModifiedDataset(self, fileName):
        return pd.read_csv(fileName)