import pyttsx3 as pp

class Speech():

    def __init__(self,word):
        self.took = pp.init()
        self.word = word

    def speech(self):
        self.took.say(self.word)
        self.took.runAndWait()

