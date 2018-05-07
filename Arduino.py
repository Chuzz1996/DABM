# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:52:44 2018

@author: PSIM
"""
import serial
import serial.tools.list_ports

class Arduino:

        #Configuración usada serial.Serial("COM3",9600,timeout=1.0)
        '''
        El timeout (tiempo máximo de espera para una lectura).
        Es importante poner un valor mayor que 0 para que en caso de error la lectura no «se cuelgue»
        indefinidamente.
        '''
        def __init__(self,puerto,baudrate):
            self._puertoSerial = serial.Serial(puerto,baudrate)
            self._puertoSerial.close()
            self._puertoSerial.open()
                
        def LeerDatos(self):
            return float(self._puertoSerial.readline().decode().strip())

        def EnviarDatos(self,character):
            self._puertoSerial.write(character.encode())
                
        def RevisarConexionArduino(self):
            # 0 si no hay un serial conectado, mayor a 0 si hay almenos un serial conectado
            return (len(list(serial.tools.list_ports.comports()))>0)

