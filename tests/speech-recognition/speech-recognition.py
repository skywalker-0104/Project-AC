"""
Author: Master Skywalker
Purpose: Project-Humanoid
Stardate: 12021.284.15:04:32

"""

# text to speech/voice engine

import speech_recognition as sr
import pyttsx3

# Recognize
r = sr.Recognizer()


# Text to speech function
def Speak(command):
    # Initialize the engine
    engine = pyttsx3.init()

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

    engine.say(command)
    engine.runAndWait() 


# Use microphone for audio input
with sr.Microphone() as SourceTwo:
    # Wait for a second and let the recognizer adjust the energy threshold based on the surrounding noise level
    r.adjust_for_ambient_noise(SourceTwo, duration=0.2)

    # Listen to the user
    AudioTwo = r.listen(SourceTwo)

    # Using google to recognize audio
    UserVoice = r.recognize_google(AudioTwo)
    UserVoice = UserVoice.lower()


print(UserVoice)
Speak(UserVoice)







