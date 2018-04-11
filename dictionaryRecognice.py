from voiceRecognition import *

class dictionaryRecognice:

    def __init__(self):
        self.lamp = {'lamp','on','lights','lights on','light'}

    def has(self,word):
        return self.lamp.__contains__(word)

