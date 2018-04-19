import string
import speech_recognition as sr

class voiceRecognition:

    def __init__(self):
        self.r = sr.Recognizer()

    def captureVoice(self):
        with sr.Microphone() as source:
            print("Say somethig: ")
            audio = self.r.listen(source)
            return self.r.recognize_google(audio)

        

