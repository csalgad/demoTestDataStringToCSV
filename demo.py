#IMPORT libraries
import string
import random
import csv

#*****************************************************************************************************#
#DEFINITIONS

#FUNCTION definition
#main: Main function
def main():
    #Instantiate a map
    tempDataMap = test_data_create()

    #Call Export CSV
    export_to_csv(tempDataMap, 'testOutput.csv')

#FUNCTION definition
#test_data_create: Returns a map of test data
def test_data_create():
    #Uppercase letters in alphabet
    alphabet = string.ascii_uppercase
    dataMap = {}

    #For each letter in alphabet
    for letter in alphabet:
        #Pick random number
        random_number = random.randint(1, 100)

        #Assign map for 'letter' to 'random number'
        dataMap[letter] = random_number

    #Return a map
    return dataMap        

#FUNCTION definition
#export_to_csv: Convert a map to a table and save as CSV 
def export_to_csv(data, filename):
    #Get keys & values
    keys = list(data.keys())
    values = list(data.values())

    #Open file and write to tit
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Key', 'Value'])
        for i in range(len(keys)):
            writer.writerow([keys[i], values[i]])


#**********************************************************************************************************#
#MAIN script

#Run main function
main()