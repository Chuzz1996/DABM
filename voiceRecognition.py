import string
import speech_recognition as sr
from threading import Thread
import socket

class voiceRecognition(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.s = socket.socket()
        self.s.connect(("localhost",6000))
        self.r = sr.Recognizer()

    def captureVoice(self):
        with sr.Microphone() as source:
            print("Say somethig: ")
            audio = self.r.listen(source)
            self.s.send(self.r.recognize_google(audio).encode("utf-8"))
            inputdata = self.s.recv(1024)
            print(inputdata)

    def run():
        self.captureVoice()
        
def main():
    x = voiceRecognition()
    x.start()
main()
