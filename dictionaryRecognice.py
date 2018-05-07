from voiceRecognition import *

class dictionaryRecognice:

    def __init__(self):
        self.lamp = {'lamp','on','lights','lights on','light'}
        self.dictionary = {}
	
    def setLanguagesAndWords(self):
        self.dictionary["EN"] = ["on","off","1","2"]
        self.dictionary["ES"] = ["encender luz","apagar luz","activar ventilador","detener ventilador","hola"]
        

    def containESdictionary(self,word):
        try:
            index = self.dictionary["EN"].index(word)
            return index
        except ValueError:
            return -1

