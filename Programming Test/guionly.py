#############################################
###### QLUE PROGRAMMING TECHNICAL TEST ######
########## HANSEL MATTHEW FTUI'18 ###########
#############################################

#Gui Library
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5 import QtGui

#System library
import sys

#Import logo resource file
import logo_rc

#Serial library for communicating to microcontroller (arduino)
import serial

#Declare serial port and baud rate (replace as needed but must be the same value as the value in the microcontroller)
# serialPort = serial.Serial(port = "COM3", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
# serialString = ""  # Used to hold data coming over UART

#Make GUI class
class sensor_gui (QMainWindow) :
    def __init__(self):
        #Load qt & gui
        QMainWindow.__init__(self)
        loadUi("sensorgui.ui",self)

        #Gui title & logo
        self.setWindowTitle("QLUE Programming Test")
        
        #Display gui
        self.show()
        
        #Button method
        self.TombolLampOn.clicked.connect(self.lampOn_pressed)
        self.TombolLampOff.clicked.connect(self.lampOff_pressed)

    #Button ON Pressed Function
    def lampOn_pressed(self):
        #Display ON di GUI
        self.output_lampstate.setText("ON")
        state = 1
        serialPort.write(bytes(state, 'utf-8'))
    
    #Button OFF Pressed Function
    def lampOff_pressed(self):
        #Display OFF di GUI
        self.output_lampstate.setText("OFF")
        state = 0
        serialPort.write(bytes(state, 'utf-8'))

#Make GUI Object
app = QApplication([])
mainwindow = sensor_gui()
app.setQuitOnLastWindowClosed(True)

# #Sensor reading
# while 1:
#     # Wait until there is data waiting in the serial buffer
#     if serialPort.in_waiting > 0:

#         # Read data out of the buffer until a carraige return / new line is found
#         serialString = serialPort.readline()

#         # Display the data to the GUI
#         try:
#             #Split the incoming message to multiple data
#             serialString = serialString.decode("Ascii").split()

#             #Save the value into separate variable
#             photosensor = float(serialString[0])
#             humidity = float(serialString[1])
#             temperature = float(serialString[2])

#             #Display the value on the GUI
#             mainwindow.output_photosensor.setText(str(round(photosensor ,3)))
#             mainwindow.output_humidity.setText(str(round(humidity ,3)))
#             mainwindow.output_temperature.setText(str(round(temperature ,3)))

#         except:
#             pass

sys.exit(app.exec_())