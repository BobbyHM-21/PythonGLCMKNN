# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
from index import Ui_Dialog1

class Ui_Dialog(object):
    def messagebox(self,title,message):
        mess=QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def warning(self,title,message):
        mess=QtWidgets.QMessageBox()

        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def login(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        conn=pymysql.connect(host="localhost",user="root",password="",db="visual",port=3306,autocommit=True)
        cur=conn.cursor()
        query="select * from admin where username=%s and password=%s"
        data=cur.execute(query, (username,password))
        if(len(cur.fetchall())>0):
            #self.messagebox("Berhasil", "Anda telah Login")
            self.Dialog = QtWidgets.QDialog()
            self.ui = Ui_Dialog1()
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
            Dialog.hide()
        else:
            self.warning("Gagal","Masukkan Username dan Password yang benar")
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(682, 510)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 91))
        self.label.setStyleSheet("background-color: rgb(0, 129, 189);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 121, 16))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 121, 81))
        self.pushButton.setStyleSheet("border-radius:60px;\n"
"")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Logo Perpustakaan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 221, 21))
        self.label_3.setStyleSheet("font: 75 16pt \"Futura Md BT\";\n"
"color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 681, 511))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(300, 310, 41, 16))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(180, 160, 331, 281))
        self.label_6.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(240, 243, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(310, 120, 81, 81))
        self.toolButton.setStyleSheet("background-color: rgb(0, 85, 127);\n"
"border-radius:40px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../Foto/Pictures/Logo/Icon BW/Account.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 380, 241, 31))
        ####
        self.pushButton_2.clicked.connect(self.login)
        ###
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 63 12pt \"Lucida Fax\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(290, 200, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Adobe Gothic Std B\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 310, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(200, 250, 31, 31))
        self.toolButton_2.setStyleSheet("border-radius:15px;")
        self.toolButton_2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../../../Foto/Pictures/Logo/Icon BW/Account 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon2)
        self.toolButton_2.setIconSize(QtCore.QSize(30, 30))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(200, 315, 31, 31))
        self.toolButton_3.setStyleSheet("border-radius:15px;")
        self.toolButton_3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../../../Foto/Pictures/Logo/Icon BW/Gembok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon3)
        self.toolButton_3.setIconSize(QtCore.QSize(25, 25))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.toolButton.raise_()
        self.pushButton_2.raise_()
        self.label_7.raise_()
        self.lineEdit_2.raise_()
        self.toolButton_2.raise_()
        self.toolButton_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Selamat Datang"))
        self.label_3.setText(_translate("Dialog", "Perpustakaan Majene"))
        self.label_5.setText(_translate("Dialog", "Login"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Username"))
        self.toolButton.setText(_translate("Dialog", "..."))
        self.pushButton_2.setText(_translate("Dialog", "LOGIN"))
        self.label_7.setText(_translate("Dialog", "Login Admin"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
