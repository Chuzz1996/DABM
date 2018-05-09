from voiceRecognition import *
import socket
from threading import Thread

class dictionaryRecognice(Thread):

    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.lamp = {'lamp','on','lights','lights on','light'}
        self.dictionary = {}
        self.conn = conn
        self.addr = addr
        self.setLanguagesAndWords()
	
    def setLanguagesAndWords(self):
        self.dictionary["EN"] = ["on","off","1","2"]
        self.dictionary["ES"] = ["encender luz","apagar luz","activar ventilador","detener ventilador","hola"]
        
    def containESdictionary(self,word):
        try:
            index = self.dictionary["EN"].index(word)
            return index
        except ValueError:
            return -1

    def run(self):
        while True:
            input_data = self.conn.recv(1024)
            print("Recibir: ",str(input_data.decode('utf-8')))
            self.conn.send(str(self.containESdictionary(input_data.decode('utf-8'))).encode("utf-8"))
            

def main():
    s = socket.socket()
    s.bind(("localhost",6000))
    s.listen(10)
    while True:
        conn,addr = s.accept()
        c = dictionaryRecognice(conn,addr)
        c.start()
        print("se ha conectado: ",addr)
    
    
if __name__ == "__main__":
    main()
