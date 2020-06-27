#-------------------------------------------------------------------------------
# Name:        TST_Program
# Purpose:
#
# Author:      Akki
#
# Created:     27-04-2020
# Copyright:   (c) Akki 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Program to convert text to speech and speech to text (internet connection required)
# Import the required module
import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
r = sr.Recognizer()
print("-------Welcome to Text to Speech to Text Program--------\n\n-> Menu <-\n 1)Text to Speech\n 2)Speech to Text")
opt=int(input("Enter your choise:"))
if(opt==1):

    myText = input("Enter The Text Here:") # The text that you want to convert to audio

    lan = 'en'  # Language in which you want to convert

    output = gTTS(text=myText, lang=lan, slow=False) # Passing the text,speed and language to the engine

    output.save("output.mp3") # Passing the text and language to the engine,

    os.system("Start output.mp3") # Playing the converted file

elif(opt==2):
    # use the microphone as source for input.
    with sr.Microphone() as source:
        print("Speak Now:")
        audio = r.listen(source) # Initialize the recognizer

        try:

            text = r.recognize_google(audio)# Using ggogle to recognize audio
            print("Did you mean:\n  {}".format(text))# print text output
        except:
            print("Sorry could't recorgnise it")

else:
    print("Error! PLease choose again")



