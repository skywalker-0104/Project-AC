
"""
Developer: Master Skywalker
Purpose: Simple text to audio generator
Stardate: 12021.285.20:48:00

"""

import pyttsx3
engine = pyttsx3.init()


UserText = input("\nEnter the text:  ")
FileName = input("\nEnter the audio file's name with the file extention (mp3):  ")


"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        
engine.setProperty('rate', 200)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1


"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.say(UserText)
engine.save_to_file(UserText, FileName)
engine.runAndWait()

