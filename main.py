from voiceRecognition import *
from dictionaryRecognice import *

def main():
    voice = voiceRecognition()
    dictionary = dictionaryRecognice()
    dictionary.setLanguagesAndWords()
    print(dictionary.dictionary)
    while(True):
        try:
            word = voice.captureVoice()
            print("You say: "+word)
            if(word=="finish"):
                break
            check = dictionary.has(word)
        except:
            continue
        if(check==True):
            print("Contains")
        else:
            print("doesn't contains")
main()
