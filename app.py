import sys 
import PyQt5 
from PyQt5 import uic, QtWidgets
import random
qtCF= "calculadora_rand.ui"

Ui_Main_wind, QtBaseClass= uic.loadUiType(qtCF)

class Calc(QtWidgets.QMainWindow,Ui_Main_wind):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Main_wind.__init__(self)
        self.setupUi(self)
        self.boton.clicked.connect(self.calculos)

    def calculos(self):
        num_1=int(self.num_1.toPlainText())
        num_2=int(self.num_2.toPlainText())
        op =random.randint(1,6)
        result=0.0
        if op==1:
            result=num_1+num_2
        elif op==2:
            result=num_1-num_2
        elif op==3:
            result=num_1*num_2
        elif op==4:
            result=num_1/num_2
        elif op==5:
            result=num_1%num_2
        elif op==6:
            result=num_1^num_2

        res="Adivina cual ha sido la cuenta!!: "+str(result)
        self.resultado.setText(res)




