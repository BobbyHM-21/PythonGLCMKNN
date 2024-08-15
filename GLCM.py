import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math
import pandas as pd
import imutils.paths as path
from sqlalchemy import create_engine
from tqdm import tqdm 
# import mysql.connector
import pymysql
pymysql.install_as_MySQLdb()
from mysql.connector import Error

# PATH = 'Data Latih'
PATH='Data Latih - Copy'

imagePaths = sorted(list(path.list_images(PATH)))

data = []
for i in tqdm (imagePaths,desc="load"):
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
                contras+=data[i,j]*pow(i-j,2)
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

# db_data = 'mysql+mysqldb://' + 'root' + ':' + '' + '@' + 'localhost' + ':3306/' \
#         + 'skripsi' + '?charset=utf8mb4'
# engine = create_engine(db_data)

#     # Connect to the database
# connection = pymysql.connect(host='localhost',
#                             user='root',
#                             password='',
#                             db='skripsi')    

#     # create cursor
# cursor=connection.cursor()
#     # Execute the to_sql for writting DF into SQL
# df.to_sql('tbl_glcm', engine, if_exists='append', index=False)    

#     # Execute query
# sql = "SELECT * FROM `tbl_glcm`"
# cursor.execute(sql)

#     # Fetch all the records
# result = cursor.fetchall()
# for i in result:
#         print(i)

# engine.dispose()
# connection.close()

# df.head()
# df.shape
# df

# df.to_csv('newdata1.csv',index=False)
