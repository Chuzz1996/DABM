# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioProyectoDABM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
from voiceRecognition import *
from dictionaryRecognice import *
from Arduino import *
from PyQt5.QtWidgets import QWidget,QMessageBox,QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import time
from speech import *

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):

        self.voice = voiceRecognition()
        self.dictionary = dictionaryRecognice()
        self.dictionary.setLanguagesAndWords()
        self.arduinoDisponible = False
        self._ConexionArduino()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.label.setStyleSheet("background:rgb(40, 40, 40)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 271, 560))
        self.label_2.setStyleSheet("background:rgb(89, 89, 89)")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 256, 196))
        self.graphicsView.setObjectName("graphicsView")
        self.btnReconocerVoz = QtWidgets.QPushButton(self.centralwidget)
        self.btnReconocerVoz.setGeometry(QtCore.QRect(10, 220, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnReconocerVoz.setFont(font)
        self.btnReconocerVoz.setObjectName("btnReconocerVoz")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 310, 91, 101))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("border-image: url(ui/luzEner.jpg);")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 420, 91, 101))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("border-image: url(ui/ventEner.jpg);")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 350, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(440, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(570, 110, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(280, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(550, 330, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.labelLucesHab1 = QtWidgets.QLabel(self.centralwidget)
        self.labelLucesHab1.setGeometry(QtCore.QRect(300, 170, 191, 151))
        self.labelLucesHab1.setText("")
        self.labelLucesHab1.setObjectName("labelLucesHab1")
        self.labelLucesHab2 = QtWidgets.QLabel(self.centralwidget)
        self.labelLucesHab2.setGeometry(QtCore.QRect(570, 170, 191, 151))
        self.labelLucesHab2.setText("")
        self.labelLucesHab1.setStyleSheet("border-image: url(ui/bombApagado.jpg);")
        self.labelLucesHab2.setObjectName("labelLucesHab2")
        self.labelLucesHab2.setStyleSheet("border-image: url(ui/fueraServ.jpg);")
        self.labelVentiladorHab1 = QtWidgets.QLabel(self.centralwidget)
        self.labelVentiladorHab1.setGeometry(QtCore.QRect(290, 380, 191, 151))
        self.labelVentiladorHab1.setText("")
        self.labelVentiladorHab1.setStyleSheet("border-image: url(ui/ventiladorAp.jpg);")
        self.labelVentiladorHab1.setObjectName("labelVentiladorHab1")
        self.labelVentiladorHab2 = QtWidgets.QLabel(self.centralwidget)
        self.labelVentiladorHab2.setGeometry(QtCore.QRect(570, 380, 191, 151))
        self.labelVentiladorHab2.setText("")
        self.labelVentiladorHab2.setObjectName("labelVentiladorHab2")
        self.labelVentiladorHab2.setStyleSheet("border-image: url(ui/fueraServ.jpg);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        
        self.btnReconocerVoz.clicked.connect(self._ReconocerVoz)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.word = None

    
    def setWord(self,word):
        self.word = word
        if(self.word!="Acabo"):
            print(self.word)
            self.accion()
            
    def _ConexionArduino(self):
        try:
            if(not self.arduinoDisponible):
                self.arduino = Arduino("COM3",9600)
                self.arduinoDisponible = True
        except:
            self.arduinoDisponible = False
            Speech("No esta conectado el Arduino").speech()
        
    def _ReconocerVoz(self):
        self._ConexionArduino()
        if(self.arduinoDisponible==True and self.arduino.RevisarConexionArduino()==True):
            VoiceThread(voiceRecognition(),self).start()
        else:
            Speech("No esta conectado el Arduino").speech()

    def accion(self):
        self._ConexionArduino()
        if(self.arduinoDisponible==True and self.arduino.RevisarConexionArduino()==True):
            imagevoicethread = VoiceRecordImage(self.graphicsView)
            imagevoicethread.start()
            indice = self.dictionary.containESdictionary(self.word)
            if(indice >= 0):
                if(indice <= 1):
                    if(indice % 2 == 0):
                        self.arduino.EnviarDatos('L')
                        self.labelLucesHab1.setStyleSheet("border-image: url(ui/luzPrendida.jpg);")
                    else:
                        self.arduino.EnviarDatos('l')
                        self.labelLucesHab1.setStyleSheet("border-image: url(ui/bombApagado.jpg);")
                else:
                    if(indice % 2 == 0):
                        self.arduino.EnviarDatos('V')
                        self.labelVentiladorHab1.setStyleSheet("border-image: url(ui/ventiladorEncen.gif);")
                    else:
                        self.arduino.EnviarDatos('v')
                        self.labelVentiladorHab1.setStyleSheet("border-image: url(ui/ventiladorAp.jpg);")
        else:
            msg = QMessageBox()
            msg.setText("Verifique la conexión con el Arduino!!")
            msg.setWindowTitle("Mensaje")
            msg.exec()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnReconocerVoz.setText(_translate("MainWindow", "Reconocer Voz"))
        self.label_3.setText(_translate("MainWindow", ""))
        self.label_4.setText(_translate("MainWindow", ""))
        self.label_5.setText(_translate("MainWindow", "Luces"))
        self.label_6.setText(_translate("MainWindow", "Ventilador"))
        self.label_7.setText(_translate("MainWindow", "Primer Piso"))
        self.label_8.setText(_translate("MainWindow", "Luces Habitación 1"))
        self.label_9.setText(_translate("MainWindow", "Luces Habitación 2"))
        self.label_10.setText(_translate("MainWindow", "Ventilador Habitación 1"))
        self.label_11.setText(_translate("MainWindow", "Ventilador Habitación 2"))


class VoiceRecordImage(threading.Thread):
    def __init__(self, graphicsView):
        threading.Thread.__init__(self)
        self.graphicsView = graphicsView

    def run(self):
        self.graphicsView.setStyleSheet("border-image: url(ui/recVoz.jpg);")
        time.sleep(3)
        self.graphicsView.setStyleSheet("color: rgb(255, 255, 255);")

        

class VoiceThread(threading.Thread):
    def __init__(self,voice,grafig):
        threading.Thread.__init__(self)
        self.voice = voice
        self.grafig = grafig
        
    def run(self):
        try:
            self.valor = self.voice.captureVoice()
            if(self.valor=="finish" or self.valor==None):
                self.grafig.setWord("Acabo")
            else:
                self.grafig.setWord(self.valor)
            Speech(self.valor).speech()
        except:
            Speech("we cant lisent you").speech()
