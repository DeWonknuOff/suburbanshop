import os
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout, QWidget, QMessageBox, QStackedWidget, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
from datetime import datetime
import random
from PyQt5 import QtCore, QtGui, QtWidgets

class UI_login(object):
    def setupUi(self, botoniniciar):
        botoniniciar.setObjectName("botoniniciar")
        botoniniciar.resize(519, 368)
        self.label = QtWidgets.QLabel(botoniniciar)
        self.label.setGeometry(QtCore.QRect(160, 10, 221, 61))
        self.label.setStyleSheet("font: 30pt \"Urban Graffiti PERSONAL USE ONL\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(botoniniciar)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 131, 21))
        self.label_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(botoniniciar)
        self.name.setGeometry(QtCore.QRect(150, 100, 241, 20))
        self.name.setText("")
        self.name.setMaxLength(20)
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(botoniniciar)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 21))
        self.label_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(botoniniciar)
        self.password.setGeometry(QtCore.QRect(150, 130, 241, 20))
        self.password.setText("")
        self.password.setMaxLength(500)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(botoniniciar)
        self.loginbutton.setGeometry(QtCore.QRect(200, 200, 141, 41))
        self.loginbutton.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"")
        self.loginbutton.setObjectName("loginbutton")
        self.showpassword = QtWidgets.QCheckBox(botoniniciar)
        self.showpassword.setGeometry(QtCore.QRect(400, 130, 121, 17))
        self.showpassword.setStyleSheet("")
        self.showpassword.setObjectName("showpassword")
        self.label_4 = QtWidgets.QLabel(botoniniciar)
        self.label_4.setGeometry(QtCore.QRect(170, 160, 91, 16))
        self.label_4.setStyleSheet("font: 8pt \"Impact\";\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.registerbutton = QtWidgets.QPushButton(botoniniciar)
        self.registerbutton.setGeometry(QtCore.QRect(260, 160, 81, 23))
        self.registerbutton.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 8pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 8pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 8pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 8pt \"Impact\";\n"
"}\n"
"")
        self.registerbutton.setObjectName("registerbutton")
        self.label_5 = QtWidgets.QLabel(botoniniciar)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 61, 61))
        self.label_5.setStyleSheet("font: 30pt \"Urban Graffiti PERSONAL USE ONL\";")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(botoniniciar)
        QtCore.QMetaObject.connectSlotsByName(botoniniciar)

    def retranslateUi(self, botoniniciar):
        _translate = QtCore.QCoreApplication.translate
        botoniniciar.setWindowTitle(_translate("botoniniciar", "Dialog"))
        self.label.setText(_translate("botoniniciar", "Iniciar Sesión"))
        self.label_2.setText(_translate("botoniniciar", "Nombre de Usuario"))
        self.label_3.setText(_translate("botoniniciar", "Contraseña :"))
        self.loginbutton.setText(_translate("botoniniciar", "Iniciar Sesión"))
        self.showpassword.setText(_translate("botoniniciar", "Mostrar Contraseña"))
        self.label_4.setText(_translate("botoniniciar", "No tienes cuenta?"))
        self.registerbutton.setText(_translate("botoniniciar", "Registrarse"))
class Ui_item(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 104)
        self.item = QtWidgets.QWidget(Form)
        self.item.setGeometry(QtCore.QRect(0, -10, 521, 111))
        self.item.setObjectName("item")
        self.image = QtWidgets.QLabel(self.item)
        self.image.setGeometry(QtCore.QRect(30, 20, 101, 91))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\sweater0.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.name = QtWidgets.QLabel(self.item)
        self.name.setGeometry(QtCore.QRect(140, 20, 131, 91))
        self.name.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.name.setScaledContents(False)
        self.name.setWordWrap(True)
        self.name.setObjectName("name")
        self.price = QtWidgets.QLabel(self.item)
        self.price.setGeometry(QtCore.QRect(280, 60, 91, 21))
        self.price.setStyleSheet("QLabel {\n"
"    color: #f77f7f;\n"
"    \n"
"    font: 87 12pt \"Segoe UI Black\";\n"
"}\n"
"")
        self.price.setObjectName("price")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name.setText(_translate("Form", "Sudadera Oversize con Gráficos Grandes"))
        self.price.setText(_translate("Form", "$750.00"))
class Ui_storescreen(object):
    def setupUi(self, StoreScreen):
        StoreScreen.setObjectName("StoreScreen")
        StoreScreen.resize(834, 903)
        StoreScreen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cartbutton = QtWidgets.QPushButton(StoreScreen)
        self.cartbutton.setGeometry(QtCore.QRect(704, 10, 121, 41))
        self.cartbutton.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #eeeeee;\n"
"    color: #999999;\n"
"    border-color: #cccccc;\n"
"}\n"
"")
        self.cartbutton.setObjectName("cartbutton")
        self.label = QtWidgets.QLabel(StoreScreen)
        self.label.setGeometry(QtCore.QRect(120, 30, 551, 51))
        self.label.setStyleSheet("font: 81 48pt \"Akira Expanded\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StoreScreen)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 231, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\sweater0.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(StoreScreen)
        self.label_3.setGeometry(QtCore.QRect(290, 140, 231, 241))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\sweater1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(StoreScreen)
        self.label_4.setGeometry(QtCore.QRect(550, 140, 231, 241))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\sweater2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(StoreScreen)
        self.label_5.setGeometry(QtCore.QRect(240, 510, 291, 291))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\sweater3.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.addbutton2 = QtWidgets.QPushButton(StoreScreen)
        self.addbutton2.setGeometry(QtCore.QRect(390, 460, 131, 31))
        self.addbutton2.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"")
        self.addbutton2.setObjectName("addbutton2")
        self.addbutton3 = QtWidgets.QPushButton(StoreScreen)
        self.addbutton3.setGeometry(QtCore.QRect(650, 460, 131, 31))
        self.addbutton3.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"")
        self.addbutton3.setObjectName("addbutton3")
        self.addbutton4 = QtWidgets.QPushButton(StoreScreen)
        self.addbutton4.setGeometry(QtCore.QRect(390, 830, 131, 31))
        self.addbutton4.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"")
        self.addbutton4.setObjectName("addbutton4")
        self.addbutton1 = QtWidgets.QPushButton(StoreScreen)
        self.addbutton1.setGeometry(QtCore.QRect(130, 460, 131, 31))
        self.addbutton1.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"")
        self.addbutton1.setObjectName("addbutton1")
        self.label_6 = QtWidgets.QLabel(StoreScreen)
        self.label_6.setGeometry(QtCore.QRect(30, 430, 91, 21))
        self.label_6.setStyleSheet("QLabel {\n"
"    color: #f77f7f;\n"
"    \n"
"    font: 87 12pt \"Segoe UI Black\";\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(StoreScreen)
        self.label_7.setGeometry(QtCore.QRect(30, 380, 241, 51))
        self.label_7.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(StoreScreen)
        self.label_8.setGeometry(QtCore.QRect(280, 430, 91, 21))
        self.label_8.setStyleSheet("QLabel {\n"
"    color: #f77f7f;\n"
"    \n"
"    font: 87 12pt \"Segoe UI Black\";\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(StoreScreen)
        self.label_9.setGeometry(QtCore.QRect(280, 380, 241, 51))
        self.label_9.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(StoreScreen)
        self.label_10.setGeometry(QtCore.QRect(550, 430, 91, 21))
        self.label_10.setStyleSheet("QLabel {\n"
"    color: #f77f7f;\n"
"    \n"
"    font: 87 12pt \"Segoe UI Black\";\n"
"}\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(StoreScreen)
        self.label_11.setGeometry(QtCore.QRect(550, 380, 241, 51))
        self.label_11.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(StoreScreen)
        self.label_12.setGeometry(QtCore.QRect(280, 780, 241, 51))
        self.label_12.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";")
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(StoreScreen)
        self.label_13.setGeometry(QtCore.QRect(280, 830, 91, 21))
        self.label_13.setStyleSheet("QLabel {\n"
"    color: #f77f7f;\n"
"    \n"
"    font: 87 12pt \"Segoe UI Black\";\n"
"}\n"
"")
        self.label_13.setObjectName("label_13")
        self.closesession = QtWidgets.QPushButton(StoreScreen)
        self.closesession.setGeometry(QtCore.QRect(660, 850, 161, 41))
        self.closesession.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #eeeeee;\n"
"    color: #999999;\n"
"    border-color: #cccccc;\n"
"}\n"
"")
        self.closesession.setObjectName("closesession")

        self.retranslateUi(StoreScreen)
        QtCore.QMetaObject.connectSlotsByName(StoreScreen)

    def retranslateUi(self, StoreScreen):
        _translate = QtCore.QCoreApplication.translate
        StoreScreen.setWindowTitle(_translate("StoreScreen", "Tienda de Sudaderas"))
        self.cartbutton.setText(_translate("StoreScreen", "🛒 Carrito"))
        self.label.setText(_translate("StoreScreen", "SUDADERAS"))
        self.addbutton2.setText(_translate("StoreScreen", "Agregar"))
        self.addbutton3.setText(_translate("StoreScreen", "Agregar"))
        self.addbutton4.setText(_translate("StoreScreen", "Agregar"))
        self.addbutton1.setText(_translate("StoreScreen", "Agregar"))
        self.label_6.setText(_translate("StoreScreen", "$750.00"))
        self.label_7.setText(_translate("StoreScreen", "Sudadera Oversize con Gráficos Grandes"))
        self.label_8.setText(_translate("StoreScreen", "$1100.00"))
        self.label_9.setText(_translate("StoreScreen", "Sudadera con Parche Bordado + Capucha Forrada"))
        self.label_10.setText(_translate("StoreScreen", "$950.00"))
        self.label_11.setText(_translate("StoreScreen", "Sudadera Tie-Dye con Zipper Lateral"))
        self.label_12.setText(_translate("StoreScreen", "Sudadera Minimalista con Toques Techwear"))
        self.label_13.setText(_translate("StoreScreen", "$1400.00"))
        self.closesession.setText(_translate("StoreScreen", "Cerrar Sesión"))
class Ui_registerscreen(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(498, 369)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 10, 221, 61))
        self.label.setStyleSheet("font: 30pt \"Urban Graffiti PERSONAL USE ONL\";")
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(170, 80, 241, 20))
        self.name.setText("")
        self.name.setMaxLength(20)
        self.name.setObjectName("name")
        self.text = QtWidgets.QLabel(Dialog)
        self.text.setGeometry(QtCore.QRect(30, 80, 131, 21))
        self.text.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.text.setObjectName("text")
        self.text2 = QtWidgets.QLabel(Dialog)
        self.text2.setGeometry(QtCore.QRect(30, 110, 131, 21))
        self.text2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.text2.setObjectName("text2")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(170, 110, 241, 20))
        self.password.setText("")
        self.password.setMaxLength(20)
        self.password.setObjectName("password")
        self.signupbutton = QtWidgets.QPushButton(Dialog)
        self.signupbutton.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.signupbutton.setObjectName("signupbutton")
        self.text2_2 = QtWidgets.QLabel(Dialog)
        self.text2_2.setGeometry(QtCore.QRect(30, 140, 141, 21))
        self.text2_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.text2_2.setObjectName("text2_2")
        self.confirm = QtWidgets.QLineEdit(Dialog)
        self.confirm.setGeometry(QtCore.QRect(170, 140, 241, 20))
        self.confirm.setText("")
        self.confirm.setMaxLength(20)
        self.confirm.setObjectName("confirm")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 300, 61, 61))
        self.label_5.setStyleSheet("font: 30pt \"Urban Graffiti PERSONAL USE ONL\";")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("C:\\Users\\dewonknu\\Downloads\\femtanyl\\software\\p2\\hayimishop\\logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Registrarse"))
        self.text.setText(_translate("Dialog", "Nombre De Usuario :"))
        self.text2.setText(_translate("Dialog", "Contraseña :"))
        self.signupbutton.setText(_translate("Dialog", "Crear Cuenta"))
        self.text2_2.setText(_translate("Dialog", "Confirmar Contraseña :"))
class UI_cart(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 907)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(290, 0, 311, 61))
        self.label.setStyleSheet("font: 30pt \"Urban Graffiti PERSONAL USE ONL\";")
        self.label.setObjectName("label")
        self.buyall = QtWidgets.QPushButton(Dialog)
        self.buyall.setGeometry(QtCore.QRect(460, 850, 161, 41))
        self.buyall.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #eeeeee;\n"
"    color: #999999;\n"
"    border-color: #cccccc;\n"
"}")
        self.buyall.setObjectName("buyall")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 850, 111, 51))
        self.label_3.setStyleSheet("font: 81 16pt \"Akira Expanded\";")
        self.label_3.setObjectName("label_3")
        self.total = QtWidgets.QLabel(Dialog)
        self.total.setGeometry(QtCore.QRect(150, 850, 111, 51))
        self.total.setStyleSheet("font: 81 16pt \"Akira Expanded\";")
        self.total.setObjectName("total")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(680, 840, 131, 51))
        self.back.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"}")
        self.back.setObjectName("back")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(20, 50, 801, 771))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.contents = QtWidgets.QWidget()
        self.contents.setGeometry(QtCore.QRect(0, 0, 799, 769))
        self.contents.setObjectName("contents")
        self.scrollLayout = QtWidgets.QVBoxLayout(self.contents)
        self.scrollLayout.setSpacing(10)
        self.scrollLayout.setObjectName("scrollLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollLayout.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.contents)
        self.deletecart = QtWidgets.QPushButton(Dialog)
        self.deletecart.setGeometry(QtCore.QRect(260, 850, 161, 41))
        self.deletecart.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #eeeeee;\n"
"    color: #999999;\n"
"    border-color: #cccccc;\n"
"}")
        self.deletecart.setObjectName("deletecart")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Carro de Compras"))
        self.buyall.setText(_translate("Dialog", "Comprar Todo"))
        self.label_3.setText(_translate("Dialog", "Total :"))
        self.total.setText(_translate("Dialog", "0"))
        self.back.setText(_translate("Dialog", "Regresar"))
        self.deletecart.setText(_translate("Dialog", "Borrar Carrito"))
class UI_ticket(object):
    def setupUi(self, TicketScreen):
        TicketScreen.setObjectName("TicketScreen")
        TicketScreen.resize(600, 728)
        self.verticalLayout = QtWidgets.QVBoxLayout(TicketScreen)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ticketHeader = QtWidgets.QLabel(TicketScreen)
        self.ticketHeader.setStyleSheet("font-weight: bold; font-size: 18px;")
        self.ticketHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.ticketHeader.setObjectName("ticketHeader")
        self.verticalLayout.addWidget(self.ticketHeader)
        self.scrollArea = QtWidgets.QScrollArea(TicketScreen)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.ticketContents = QtWidgets.QWidget()
        self.ticketContents.setGeometry(QtCore.QRect(0, 0, 580, 616))
        self.ticketContents.setObjectName("ticketContents")
        self.ticketListWidget = QtWidgets.QVBoxLayout(self.ticketContents)
        self.ticketListWidget.setObjectName("ticketListWidget")
        self.scrollArea.setWidget(self.ticketContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.accept = QtWidgets.QPushButton(TicketScreen)
        self.accept.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"}")
        self.accept.setObjectName("accept")
        self.verticalLayout.addWidget(self.accept)
        self.ticketFooter = QtWidgets.QLabel(TicketScreen)
        self.ticketFooter.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.ticketFooter.setAlignment(QtCore.Qt.AlignRight)
        self.ticketFooter.setObjectName("ticketFooter")
        self.verticalLayout.addWidget(self.ticketFooter)

        self.retranslateUi(TicketScreen)
        QtCore.QMetaObject.connectSlotsByName(TicketScreen)

    def retranslateUi(self, TicketScreen):
        _translate = QtCore.QCoreApplication.translate
        TicketScreen.setWindowTitle(_translate("TicketScreen", "Ticket"))
        self.ticketHeader.setText(_translate("TicketScreen", "[SubUrban Shop]"))
        self.accept.setText(_translate("TicketScreen", "Aceptar"))
        self.ticketFooter.setText(_translate("TicketScreen", "Total: $0\\nIVA: $0"))
class UI_buy(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 403)
        self.confirmbuy = QtWidgets.QPushButton(Dialog)
        self.confirmbuy.setGeometry(QtCore.QRect(200, 280, 201, 41))
        self.confirmbuy.setStyleSheet("QPushButton {\n"
"    background-color: #ffffff;\n"
"    color: #000000;\n"
"    border: 2px solid #000000;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #000000;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #222222;\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #eeeeee;\n"
"    color: #999999;\n"
"    border-color: #cccccc;\n"
"}")
        self.confirmbuy.setObjectName("confirmbuy")
        self.cancelbuy = QtWidgets.QPushButton(Dialog)
        self.cancelbuy.setGeometry(QtCore.QRect(430, 280, 171, 51))
        self.cancelbuy.setStyleSheet("QPushButton {\n"
"    background-color: #000000;\n"
"    color: #888888;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"    font: 14pt \"Impact\";\n"
"}\n"
"QPushButton:hover {\n"
"    color: #ffffff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #111111;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #222222;\n"
"    color: #555555;\n"
"}")
        self.cancelbuy.setObjectName("cancelbuy")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 150, 211, 21))
        self.label.setStyleSheet("font: 15pt \"PaybAck\";")
        self.label.setObjectName("label")
        self.creditcard = QtWidgets.QLineEdit(Dialog)
        self.creditcard.setGeometry(QtCore.QRect(260, 150, 541, 21))
        self.creditcard.setObjectName("creditcard")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 40, 551, 51))
        self.label_2.setStyleSheet("font: 81 48pt \"Akira Expanded\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 211, 21))
        self.label_3.setStyleSheet("font: 15pt \"PaybAck\";")
        self.label_3.setObjectName("label_3")
        self.direction = QtWidgets.QLineEdit(Dialog)
        self.direction.setGeometry(QtCore.QRect(260, 200, 541, 21))
        self.direction.setObjectName("direction")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.confirmbuy.setText(_translate("Dialog", "Confirmar compra"))
        self.cancelbuy.setText(_translate("Dialog", "Cancelar Compra"))
        self.label.setText(_translate("Dialog", "Tarjeta de Credito"))
        self.label_2.setText(_translate("Dialog", "Cobro"))
        self.label_3.setText(_translate("Dialog", "Direccion"))

USERS_FILE = "users.json"
CART_FILE = "cart.json"
TICKETS_FILE = "tickets.json"

def load_tickets():
    if os.path.exists(TICKETS_FILE):
        with open(TICKETS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tickets(tickets):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=4)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def save_cart(user_id, cart_items):
    total = sum(item["price"] for item in cart_items)
    data = {}
    if os.path.exists(CART_FILE):
        try:
            with open(CART_FILE, "r") as f:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
        except json.JSONDecodeError:
            data = {}
    
    data[user_id] = {
        "items": cart_items,
        "total": total
    }

    with open(CART_FILE, "w") as f:
        json.dump(data, f)

def load_cart(user_id):
    try:
        if os.path.exists(CART_FILE):
            with open(CART_FILE, "r") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data.get(user_id, {"items": [], "total": 0})
    except Exception as e:
        print(f"Error cargando carrito: {e}")
    return {"items": [], "total": 0}

products = [
    {"name": "Sudadera Oversize con Gráficos Grandes", "price": 750,"id":"0"},
    {"name": "Sudadera con Parche Bordado + Capucha Forrada", "price": 1100,"id":"1"},
    {"name": "Sudadera Tie-Dye con Zipper Lateral", "price": 950,"id":"2"},
    {"name": "Sudadera Minimalista con Toques Techwear", "price": 1400,"id":"3"}
]
TotalPrice = 0
ShowPass = False

class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = UI_login()
        self.ui.setupUi(self)
        self.ui.loginbutton.clicked.connect(self.login)
        self.ui.registerbutton.clicked.connect(self.goto_register)
        self.ui.showpassword.clicked.connect(self.togglepassword)
    
    def reset_fields(self):
        self.ui.name.clear()
        self.ui.password.clear()
        self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)


    def togglepassword(self):
        global ShowPass
        if ShowPass == False:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            ShowPass = True
        else:
            self.ui.password.setEchoMode(QtWidgets.QLineEdit.Password)
            ShowPass = False

    def login(self):
        users = load_users()
        name = self.ui.name.text()
        password = self.ui.password.text()
        for user_id, user in users.items():
            if user["name"] == name and user["password"] == password:
                store = StoreScreen(user_id)
                widget.addWidget(store)
                widget.setCurrentWidget(store)
                login = widget.widget(0)
                login.reset_fields()
                return
        QMessageBox.warning(self, "Error", "Correo o contraseña incorrectos")


    def goto_register(self):
        register = RegisterScreen()
        widget.addWidget(register)
        widget.setCurrentWidget(register)

class RegisterScreen(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_registerscreen()
        self.ui.setupUi(self)
        self.ui.signupbutton.clicked.connect(self.register)

    def register(self):
        users = load_users()
        name = self.ui.name.text()
        password = self.ui.password.text()
        confirm = self.ui.confirm.text()
        if password != confirm:
            QMessageBox.warning(self, "Error", "Las contraseñas no coinciden")
            return
        user_id = str(len(users) + 1)
        users[user_id] = {"name": name, "password": password}
        save_users(users)
        QMessageBox.information(self, "Éxito", "Cuenta creada correctamente")
        widget.setCurrentIndex(0)

class StoreScreen(QDialog):
    def __init__(self, user_id):
        super().__init__()
        self.ui = Ui_storescreen()
        self.ui.setupUi(self)
        self.user_id = user_id
        carrito_data = load_cart(user_id)
        self.carrito = carrito_data["items"]


        self.ui.addbutton1.clicked.connect(lambda: self.add_to_cart(products[0]))
        self.ui.addbutton2.clicked.connect(lambda: self.add_to_cart(products[1]))
        self.ui.addbutton3.clicked.connect(lambda: self.add_to_cart(products[2]))
        self.ui.addbutton4.clicked.connect(lambda: self.add_to_cart(products[3]))
        self.ui.cartbutton.clicked.connect(self.show_cart)
        self.ui.closesession.clicked.connect(self.logout)

        widget.setFixedSize(834, 903)

    def add_to_cart(self, product):
        self.carrito.append(product)
        save_cart(self.user_id, self.carrito)
        QMessageBox.information(self, "Agregado", f"{product['name']} añadido al carrito.")

    def show_cart(self):
        cart = CartScreen(self.user_id)
        cart.store_screen = self
        widget.addWidget(cart)
        widget.setCurrentWidget(cart)
    
    def logout(self):
        widget.setCurrentIndex(0)
        widget.setFixedSize(519, 368)

class CartScreen(QDialog):
    def __init__(self, user_id):
        super().__init__()
        self.ui = UI_cart()
        self.ui.setupUi(self)
        self.user_id = user_id
        carrito_data = load_cart(user_id)
        self.carrito = carrito_data["items"]
        self.total_price = carrito_data["total"]


        self.ui.back.clicked.connect(self.go_back)
        self.ui.deletecart.clicked.connect(self.delete_cart)
        self.ui.buyall.clicked.connect(self.buy_all)

        self.populate_cart()
        
        self.setMinimumSize(675, 590)
        self.setMaximumSize(16777215, 16777215)
        
        self.ui.total.setText(f"${self.total_price}")
    
    def populate_cart(self):
        contents = self.ui.scrollArea.widget()

        for child in contents.findChildren(QWidget):
            child.setParent(None)

        y_offset = 0
        item_height = 120

        for item in self.carrito:
            item_container_widget = QtWidgets.QWidget(contents)
            item_ui = Ui_item()
            item_ui.setupUi(item_container_widget)

            item_ui.name.setText(item["name"])
            item_ui.price.setText(f"${item['price']}")
            img_path = f"sweater{item['id']}.png"
            if os.path.exists(img_path):
                pixmap = QPixmap(img_path)
                item_ui.image.setPixmap(pixmap.scaled(100, 100))

            item_container_widget.setGeometry(0, y_offset, contents.width(), item_height)
            y_offset += item_height + 10

        contents.setMinimumHeight(y_offset)
    
    def delete_cart(self):
        self.carrito = []
        save_cart(self.user_id, self.carrito)
        QMessageBox.information(self, "Carrito eliminado", "Tu carrito ha sido vaciado.")
        self.populate_cart()

    def buy_all(self):
        if not self.carrito:
            QMessageBox.warning(self, "Carrito vacío", "No hay productos para comprar.")
            return

        buy_screen = BuyScreen(self.user_id, self.carrito, self.total_price, self)
        widget.addWidget(buy_screen)
        widget.setCurrentWidget(buy_screen)

    def go_back(self):
        store = StoreScreen(self.user_id)
        widget.addWidget(store)
        widget.setCurrentWidget(store)
        widget.setFixedSize(834, 903)

class BuyScreen(QDialog):
    def __init__(self, user_id, carrito, total, cart_screen):
        super().__init__()
        self.ui = UI_buy()
        self.ui.setupUi(self)
        self.user_id = user_id
        self.carrito = carrito
        self.total = total
        self.cart_screen = cart_screen

        self.ui.cancelbuy.clicked.connect(self.cancel_purchase)
        self.ui.confirmbuy.clicked.connect(self.confirm_purchase)

    def cancel_purchase(self):
        widget.setCurrentWidget(self.cart_screen)

    def confirm_purchase(self):
        ticket_screen = TicketScreen(self.user_id, self.carrito, self.total)
        widget.addWidget(ticket_screen)
        widget.setCurrentWidget(ticket_screen)

class TicketScreen(QDialog):
    def __init__(self, user_id, carrito, total):
        super().__init__()
        self.ui = UI_ticket()
        self.ui.setupUi(self)
        self.user_id = user_id

        tickets = load_tickets()
        existing_ids = {t["id"] for t in tickets}

        ticket_id = random.randint(1000, 9999)
        while ticket_id in existing_ids:
            ticket_id = random.randint(1000, 9999)

        fecha = datetime.now().strftime("%d/%m/%Y")
        self.ui.ticketHeader.setText(f"[SubUrban Shop]\nVenta realizada el {fecha}\nTicket {ticket_id}\n------------------------")

        iva_total = 0
        layout = self.ui.ticketListWidget

        for item in carrito:
            nombre = item["name"]
            precio = item["price"]
            item_id = item["id"]
            iva = round(precio * 0.16, 2)
            iva_total += iva

            label = QLabel(f"{nombre}  {item_id}  ${precio}")
            layout.addWidget(label)

        self.ui.ticketFooter.setText(f"Total: ${total}\nIVA: ${round(iva_total, 2)}")


        tickets.append({
            "id": ticket_id,
            "user_id": user_id,
            "fecha": fecha,
            "items": carrito,
            "total": total,
            "iva_total": round(iva_total, 2)
        })
        save_tickets(tickets)

        self.ui.accept.clicked.connect(self.back_to_cart)

    def back_to_cart(self):
        save_cart(self.user_id, [])
        cart_screen = CartScreen(self.user_id)
        widget.addWidget(cart_screen)
        widget.setCurrentWidget(cart_screen)
        QMessageBox.information(self, "Gracias", "Gracias por su compra.")

app = QApplication([])
app.setApplicationName("Suburban Shop")
app.setWindowIcon(QtGui.QIcon("logo.png"))
widget = QStackedWidget()
login = LoginScreen()
widget.addWidget(login)
widget.setFixedSize(600, 400)
widget.show()
app.exec_()
