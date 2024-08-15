import sys
import matplotlib.image as mpimg
import numpy as np
import cv2
import os 
import imutils.paths as path
import cv2 as cv
import matplotlib.pyplot as plt
import math
import pandas as pd
from tqdm import tqdm 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


from PyQt5 import QtCore 
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFileDialog , QTableView , QTableWidgetItem
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
# from cv2 import cvtColor

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
sns.set()

#database
import mysql.connector as mc
from mysql.connector import Error


############################################ AWAL ######################################################
#Tampilan Awal
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('./GUI/welcomescreen.ui',self)
        self.login.clicked.connect(self.gotologin)
        self.User.clicked.connect(self.user)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def user(self):
        user = Klasifikasi()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex()+1)

#LOGIN
class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi('./GUI/login.ui',self)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        print("Selamat Datang")

    def loginfunction(self):
        user = self.emailfield.text()
        password = self.passwordfield.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please input all fields.")

        else:
            conn = mc.connect(host='localhost',
                                         database='skripsi',
                                         user='root',
                                         password='')
            cur = conn.cursor()
            query = 'SELECT sandi FROM tbl_user WHERE user =\''+user+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                menuutama = MenuUtama()
                widget.addWidget(menuutama)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                print("Successfully logged in.")
                self.error.setText("")
            else:
                self.error.setText("Invalid username or password")

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi('./GUI/fillprofile.ui',self)
        self.image.setPixmap(QPixmap('placeholder.png'))
         
############################################ Menu Utama Admin ##########################################################
class MenuUtama(QDialog):
    def __init__(self):
        super(MenuUtama, self).__init__()
        loadUi('./GUI/MenuAdmin.ui',self)
        widget.setFixedHeight(900)
        widget.setFixedWidth(1400)
        self.klasifikasi.clicked.connect(self.clas)
        # self.data_latih.clicked.connect(self.train)
        self.logout.clicked.connect(self.keluar)
        # self.create.clicked.connect(self.gotocreate)
    
    def keluar(self):
        logout = LoginScreen()
        widget.addWidget(logout)  
        widget.setCurrentIndex(widget.currentIndex() + 1)
    
    def clas(self):
        kelas = Klasifikasi()
        widget.addWidget(kelas)  
        widget.setCurrentIndex(widget.currentIndex() + 1)     

class Klasifikasi(QDialog):
    def __init__(self):
        super(Klasifikasi, self).__init__()
        loadUi('./GUI/MenuKlasifikasi.ui',self)
        self.select_data()
        
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1500)
        self.inputcitra.clicked.connect(self.InputCitra)
        self.reset.clicked.connect(self.clear)
        
    def loadImage(self, fname):
        self.fNama.setText(fname)
        self.image = cv2.imread(fname)
        self.tmp = self.image
        self.displayImage(1)
        self.segmentasi.clicked.connect(self.Segmentasi)
        self.glcm.clicked.connect(self.Glcm)
    
    def select_data(self):
        try:
            mydb = mc.connect(

                host="localhost",
                user="root",
                password="",
                database='skripsi'
            )

            mycursor = mydb.cursor()

            mycursor.execute("SELECT * FROM {} ".format('tbl_glcm'))
            
            result = mycursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                print(row_number)
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")

    def clear(self):
        # loadUi('./GUI/MenuKlasifikasi.ui',self)
        if os.path.exists("./grayscale.jpg"):
            os.remove("./grayscale.jpg")
            print("File deleted !") 
        else:
            print("File doesnot exist !") 

        if os.path.exists( "./testing.csv" ):
            os.remove("./testing.csv")
            print("File dihapus !") 
        else:
            print("File doesnot exist !") 

        self.imgLabel2.clear()
        self.imgLabel.clear()
        self.fNama.setText("")
        self.textEdit_2.setText("")
    def InputCitra(self):
        fname, filter = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\Users\ROG\Desktop\FIX', "Image Files (*)")
        if fname:
            self.loadImage(fname)
        else:
            print("Invalid Image")

    def displayImage(self, window=1):
        qformat = QImage.Format_Indexed8

        if len(self.image.shape) == 3:
            if(self.image.shape[2]) == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        img = QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)

        img = img.rgbSwapped() 
        if window == 1:
            self.imgLabel.setPixmap(QPixmap.fromImage(img))
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        if window == 2:
             self.imgLabel2.setPixmap(QPixmap.fromImage(img))
             self.imgLabel2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
    def Segmentasi(self):
        self.image = self.tmp
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.displayImage(2)
        self.saveImage()
       
    def saveImage(self):
        cv.imwrite('./train/grayscale.jpg',self.image)
        print("Sukses")

    def Glcm(self):
        PATH = 'train'
        imagePaths = sorted(list(path.list_images(PATH)))

        data = []
        for i in tqdm (imagePaths,desc="Memuat"):
            imgg=cv.imread(i)
            img=cv.cvtColor(imgg,cv.COLOR_BGR2GRAY)
            a = cv.resize(img, (300,300))
            data.append(a)

        def derajat0 (img):
            max = np.max(img)
            imgTmp = np.zeros([max+1,max+1])
            for i in range (len(img)):
                for j in range (len(img[i])-1):
                    imgTmp[img[i,j],img[i,j+1]] += 1
            transpos = np.transpose(imgTmp)
            data= imgTmp+transpos

            tmp=0
            for i in range (len(data)):
                for j in range (len(data)):
                    tmp+=data[i,j]
            for i in range (len(data)):
                for j in range (len(data)):
                    data[i,j]/=tmp
            return data

        def derajat45 (img):
            max=np.max (img)
            imgTmp = np.zeros([max+1,max+1])
            for i in range (len(img)-1):
                for j in range(len(img[i])-1):
                    imgTmp[img[i+1,j],img[i,j+1]] += 1
            transpos = np.transpose(imgTmp)
            data= imgTmp+transpos 

            tmp=0
            for i in range (len(data)):
                for j in range (len(data)):
                    tmp+=data[i,j]
            for i in range (len(data)):
                for j in range (len(data)):
                    data[i,j]/=tmp
            return data
            
        def derajat90 (img):
            max = np.max(img)
            imgTmp = np.zeros([max+1,max+1])
            for i in range (len(img)-1):
                for j in range (len(img[i])):
                    imgTmp[img[i+1,j],img[i,j]] += 1
            transpos= np.transpose(imgTmp)
            data = imgTmp+transpos

            tmp=0
            for i in range (len(data)):
                for j in range(len(data)):
                    tmp+=data[i,j]
            for i in range (len(data)):
                for j in range (len(data)):
                    data[i,j]/=tmp
            return data

        def derajat135 (img):
            max=np.max(img)
            imgTmp = np.zeros([max+1,max+1])
            for i in range (len(img)-1):
                for j in range (len(img[i])-1):
                    imgTmp[img[i,j],img[i+1,j+1]] +=1
            transpos=np.transpose(imgTmp)
            data=imgTmp+transpos

            tmp=0
            for i in range (len(data)):
                for j in range (len(data)):
                    tmp+=data[i,j]

            for i in range (len(data)):
                for j in range (len(data)):
                    data[i,j]/=tmp
            return data
            
        hasil = []
        for i in tqdm (range(len(data)),desc='GLCM'):
                dat=[]
                dat.append(derajat0(data[i]))
                dat.append(derajat45(data[i]))
                dat.append(derajat90(data[i]))
                dat.append(derajat135(data[i]))
                hasil.append(dat)

        def contras(data):
                contras=0
                for i in range (len(data)):
                    for j in range (len(data)):
                         contras += (i-j)**2 * data[i,j] 
                        # contras+=data[i,j]*pow(i-j,2)
                return contras

        def entropy(data):
                entro=0
                for i in range (len(data)):
                    for j in range(len(data)):
                        if data[i,j]>0.0:
                            entro+=-(data[i,j]*math.log(data[i,j]))
                return entro

        def homogentitas (data):
                homogen=0
                for i in range (len(data)):
                    for j in range(len(data)):
                        homogen+=data[i,j]*(1+(pow(i-j,2)))
                return homogen
            
        def energi (data): 
                ener=0
                for i in range (len(data)):
                    for j in range(len(data)):
                        for j in range (len(data)):
                            ener += data[i,j]**2
                return ener
        def corr(data):
                corr = 0 
                xbari = 0
                xbarj = 0
                sigi = 0
                sigj = 0
                x1 = 0
                for i in range(len(data)):
                    for j in range(len(data)):
                        xbari += data[i,j] * i
                        xbarj += j * data[i,j]
                        sigi += data[i,j]*(i-xbari)**2
                        sigj += data[i,j]*(j-xbarj)**2
                        x1 += ((i-xbari)*(j-xbarj))*data[i,j]
                corr = (x1/np.sqrt(sigi*sigj))
                return corr


        data0energi=[]
        data0=[]
        x=['0','45','90','135']
        data45=[]
        data90=[]
        data135=[]
        hasilnya=[]

        for j in tqdm (range(len(hasil)),desc="Ekstraksi"):
                da=[]
                da.append(imagePaths[j])
                for i in hasil [j]:
                    dx=energi(i)
                    da.append(dx)

                    dh=homogentitas(i)
                    da.append(dh)

                    den=entropy(i)
                    da.append(den)

                    dco=contras(i)
                    da.append(dco)

                    dc=corr(i)
                    da.append(dc)

                hasilnya.append(da)

        namatabel = ['file','energy_0','homogenity_0','entropy_0','contras_0','correlation_0'
                    ,'energy_45','homogenity_45','entropy_45','contras_45','correlation_45'
                    ,'energy_90','homogenity_90','entropy_90','contras_90','correlation_90'
                    ,'energy_135','homogenity_135','entropy_135','contras_135','correlation_135']
        df = pd.DataFrame(hasilnya, columns=namatabel)


        df.to_csv('./train/testing.csv',index=False)
        print("Ekstraksi FItur Selesai")
        self.hasil_knn.clicked.connect(self.knearest)
#############proses knn###############
    def knearest(self, df):
            keluak=pd.read_csv('ekstraksiGLCM.csv')

            result = []
            for value in range (0,241):
                if value <=80:
                    result.append("Keluak Matang") 

                elif value <=159:
                    result.append("Keluak Setengah Matang") 

                elif value >=160 & value <=240 :
                    result.append("Keluak Mentah") 

                else :
                    result.append("Tidak Dapat Di klasifikasi")
            keluak['label'] = result

            data = keluak[['energy_0','homogenity_0','entropy_0','contras_0','correlation_0'
                        ,'energy_45','homogenity_45','entropy_45','contras_45','correlation_45'
                        ,'energy_90','homogenity_90','entropy_90','contras_90','correlation_90'
                        ,'energy_135','homogenity_135','entropy_135','contras_135','correlation_135']].to_numpy()
            print(data)

            label = keluak['label'].to_numpy()

            (keluak['label'].unique())

            train_clasx, test_clasx, train_clasy, test_clasy = train_test_split(data, label, test_size=0.4,random_state=42)

            neigh = KNeighborsClassifier(n_neighbors=9)
            neigh.fit(data,label)

            pred_clas = neigh.predict(test_clasx)
            # print(pred_clas)
            pred_clas.shape

            ##############PENGUJIAN########################
            keluak_uji=pd.read_csv('./train/testing.csv')
            data1 = keluak_uji[['energy_0','homogenity_0','entropy_0','contras_0','correlation_0'
                        ,'energy_45','homogenity_45','entropy_45','contras_45','correlation_45'
                        ,'energy_90','homogenity_90','entropy_90','contras_90','correlation_90'
                        ,'energy_135','homogenity_135','entropy_135','contras_135','correlation_135']].to_numpy()
            print(data1)
            
            pred_clas = neigh.predict(data1)
            print(pred_clas)
            self.textEdit_2.setText(str(pred_clas))

#main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome = WelcomeScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    try:
        welcome
        sys.exit(app.exec_())
    except:
        print("Exiting")

