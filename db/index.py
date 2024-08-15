# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_Dialog1(object):
    def messagebox(self,title,message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def selesai(self):
        nama = self.lineEdit.text()
        alamat = self.lineEdit_2.text()
        pekerjaan = self.lineEdit_4.text()
        tujuan = self.lineEdit_3.text()
        conn = pymysql.connect(host="localhost",user="root",password="",db="visual", port=3306,autocommit=True)
        cur = conn.cursor()
        query = ("insert into pengunjung(nama,alamat,pekerjaan,tujuan) values(%s,%s,%s,%s)")
        data = cur.execute(query, (nama,alamat,pekerjaan,tujuan))
        if(data):
            self.messagebox("Selamat", "Data Berhasil Ditambahkan")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(680, 510)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 681, 501))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 221, 21))
        self.label_3.setStyleSheet("font: 75 16pt \"Futura Md BT\";\n"
"color: rgb(255, 255, 0);")
        self.label_3.setObjectName("label_3")
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 681, 91))
        self.label_2.setStyleSheet("background-color: rgb(0, 129, 189);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 30, 121, 16))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(30, 110, 621, 381))
        self.label_8.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(250, 120, 191, 31))
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
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 441, 31))
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
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 250, 441, 31))
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
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 390, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(100, 157, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(100, 227, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(100, 366, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(100, 297, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Gothic Std B")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Adobe Gothic Std B\";")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 450, 241, 31))
        ###
        self.pushButton_3.clicked.connect(self.selesai)
        ###
        self.pushButton_3.setStyleSheet("background-color: rgb(0, 170, 127);\n"
"font: 63 12pt \"Lucida Fax\";\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 320, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background:transparent;\n"
"color:black;\n"
"border:none;\n"
"border-bottom:1px solid")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButton_3.raise_()
        self.lineEdit_4.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Perpustakaan Majene"))
        self.label_4.setText(_translate("Dialog", "Selamat Datang"))
        self.label_7.setText(_translate("Dialog", "BUKU PENGUNJUNG"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Nama"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Alamat"))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Tujuan"))
        self.label_9.setText(_translate("Dialog", "Nama"))
        self.label_10.setText(_translate("Dialog", "Alamat"))
        self.label_11.setText(_translate("Dialog", "Tujuan"))
        self.label_12.setText(_translate("Dialog", "Pekerjaan"))
        self.pushButton_3.setText(_translate("Dialog", "Selesai"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Pekerjaan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
