# -*- coding: utf-8 -*-
"""linear_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1deytit-Grv8_jaLco08S37MrI3_TglLA
"""

import zipfile
from google.colab import drive

drive.mount('/content/drive/')
zip_ref = zipfile.ZipFile('/content/investment.zip', 'r')
zip_ref.extractall()
zip_ref.close()

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.metrics import r2_score

from sklearn.linear_model import LinearRegression



from sklearn.model_selection import train_test_split

df = pd.read_csv('/content/investment-growth-forcast.csv')

df



x = df['Investment'].values

x = x.reshape(-1,1)

x.shape

y = df[['PFT']].values

y.shape

y =y.reshape(-1,1)

df

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=9, include_bias=False)

x_new = poly.fit_transform(x)





new_model = LinearRegression()

new_model.fit(x_new,y)

y_pred = new_model.predict(x_new)

plt.scatter(x, y)
plt.plot(x_new, y_pred)
plt.legend(['Predicted Line', 'Observed Line'])
plt.show()





r2_score(y, y_pred)



plt.figure(figsize=(26,14))
plt.plot(y_pred,'g',label="Predicted Investment Growth by month with 75% metric Accuracy using a linear model with Polynomial features")
plt.plot(y,'r',label="Past calulated Profit on investment by month")
plt.legend(loc="upper left")
plt.xlabel('Months')
plt.ylabel('Dollars')
plt.title('Predicted Investment Growth')
plt.show()