import easygui as eg
from os import sys
import regularities

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
    #TODO: fieldValues[0] is dataset, send this to regularities.py

    #select desired effect
    msg ="Choose desired predicate."
    data, predicates, rows = regularities.getDataset(fieldValues[0])
    choice = eg.choicebox(msg, title, predicates)

    #display results
    untestedConditions = regularities.findAllSubsets(rows, predicates, choice)
    provenConditions = regularities.generateDisjunction(untestedConditions, data, predicates, choice)
    result_text = ""
    for condition in provenConditions:
        result_text = result_text + '(' + ', '.join(condition) + ')\n'
    # f = open('output.txt', "r")
    # text = f.readlines()
    # f.close()
    # eg.codebox("Proven Conditions for " + str(choice), "Show File Contents", text)
    eg.codebox("Proven Conditions for " + str(choice), "Show File Contents", result_text)

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if eg.ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:  
        break