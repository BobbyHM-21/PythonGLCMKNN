import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import joblib
sns.set()

keluak=pd.read_csv('ekstraksiGLCM.csv')

# result = []
# for value in range (0,500):
#     if value <=166:
#             result.append("Keluak Matang") 
#     elif value <=330 :
#             result.append("Keluak Setengah Matang") 
#     else :
#             result.append("Keluak Mentah")
# keluak['label'] = result

# data = keluak[['energy_0','homogenity_0','entropy_0','contras_0'
#             ,'energy_45','homogenity_45','entropy_45','contras_45'
#             ,'energy_90','homogenity_90','entropy_90','contras_90'
#             ,'energy_135','homogenity_135','entropy_135','contras_135']].to_numpy()
# print(data)

result = []
for value in range (0,241):
    if value <=80:
        result.append("Keluak Matang") 

    elif value <=159:
        result.append("Keluak Setengah Matang") 

    elif value >=160 & value <=230 :
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

neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(data,label)

pred_clas = neigh.predict(test_clasx)
print(pred_clas)
pred_clas.shape

# label_mapping = dict(zip(keluak.file.unique(),keluak.file.unique()))
# label_mapping
# keluak['label'].value_counts()





