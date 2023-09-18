import speech_recognition
import pyttsx3
import wave
import json
import os

def playVoiseAssistantSppech(text_to_speech):
    return

def recordAndRecognizeAudio(*args: tuple):
    with microphone:
        recognized_data = ""
        
        recognizer.adjust_for_ambient_noise(microphone, 2)
        
        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5)
        
        except:
            print("Can you check if your microphone is On, please?")
            return None
        #*--------------------------------------------------*#
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language = "ru").lower()
            
        except speech_recognition.UnknownValueError:
            pass
        
        except speech_recognition.RequestError():
            print("Check your Internet Connection, please")
            
        
        return recognized_data
        

        
        

if __name__== "__main__":
    
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    while True:
        voice_input = recordAndRecognizeAudio()
        print(voice_input)
        
        
        
