import inline as inline
import matplotlib
import matplotlib.pyplot as plt
import sklearn
import sns as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, Imputer
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
matplotlib


dataset = pd.read_csv('data.csv')

#print(dataset) #verimizi görelim
#dataset.count()
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,88].values
#print(y)
print(X[:,9]) # yasları getirir tüm oyuncuların
print("*******************************************************")
labelencoder_X = LabelEncoder()

X[:,2] = labelencoder_X.fit_transform(X[:,2].astype(str))
X[:,4] = labelencoder_X.fit_transform(X[:,4])
X[:,7] = labelencoder_X.fit_transform(X[:,7].astype(str))
X[:,9] = labelencoder_X.fit_transform(X[:,9].astype(str))
X[:,10] = labelencoder_X.fit_transform(X[:,10].astype(str))
X[:,14] = labelencoder_X.fit_transform(X[:,14].astype(str))
X[:,18] = labelencoder_X.fit_transform(X[:,18].astype(str))
X[:,19] = labelencoder_X.fit_transform(X[:,19].astype(str))
X[:,20] = labelencoder_X.fit_transform(X[:,21].astype(str))


#print(X[:,4]) # url kısmı sayı olarak geldi
print("*******************************************************")
#print(X[:,9])  takımlar sayı olarak geldi


del dataset["ID"]
dataset = X

print(dataset)
plt.figure(figsize=(15,32))
sns.countplot(y = dataset[:,5],palette="Set2")
plt.show()