from voiceRecognition import *

class dictionaryRecognice:

    def __init__(self):
        self.lamp = {'lamp','on','lights','lights on','light'}
        self.dictionary = {}
	
    def setLanguagesAndWords(self):
        self.dictionary["EN"] = ["light on","light off","activate fan","stop fan"]
        self.dictionary["ES"] = ["encender luz","apagar luz","activar ventilador","detener ventilador"]
        

    def has(self,word):
        return self.lamp.__contains__(word)

