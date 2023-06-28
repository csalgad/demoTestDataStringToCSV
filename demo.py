#IMPORT libraries
import os
import string
import random
import csv
from google.cloud import speech

#*****************************************************************************************************#
#DEFINITIONS

#FUNCTION definition
#main: Main function
def main():
    #Call Speech-to-Text
    #HOLD# converted_text = gcloud_s2t()

    #Instantiate a map
    tempDataMap = test_data_create()

    #Debug
    print("Start of Debug: ")
    print("data_map: ", tempDataMap)

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

#FUNCTION definition
#gcloud_s2t: Google Cloud Speech-to-Text
def gcloud_s2t():
    #Google Environment variable
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_service_key.json'

    #Instantiate the speech client
    speech_client = speech.SpeechClient()

    ## SETUP ##

    #File name
    file_name = 'demo_audio.mp3'

    #Open media file and read in as byte data
    with open(file_name, 'rb') as media_file:
        #Convert to byte data
        byte_data = media_file.read()

    #Convert to audio
    audio = speech.RecognitionAudio(content = byte_data)

    #Create config
    config = speech.RecognitionConfig(
        sample_rate_hertz=48000,
        enable_automatic_punctuation=True,
        language_code='en-US'
    )

    #Transcribe audio with speech client's recognize() function
    response = speech_client.recognize()

    return response

#**********************************************************************************************************#
#MAIN script

#Run main function
main()