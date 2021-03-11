import easygui as eg
from os import sys

while 1:
    #starting page
    # title = "Causal Regularity Finder 3000"
    # eg.msgbox("Causal Regularity Finder 3000", title)

    #enter dataset
    msg ="Enter the name of your dataset."
    title = "Causal Regularity Finder 3000"
    fieldNames = ["Data Set"]
    fieldValues = []  # we start with blanks for the values
    fieldValues = eg.multenterbox(msg,title, fieldNames)
    #TODO: fieldValue[0] is dataset, send this to regularities.py

    #select desired effect
    choices = ["P", "Q", "S", "R"]
    choice = eg.choicebox(msg, title, choices)

    #display results
    f = open('output.txt', "r")
    text = f.readlines()
    f.close()
    eg.codebox("Proven Conditions for " + str(choice), "Show File Contents", text)

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:  
        break