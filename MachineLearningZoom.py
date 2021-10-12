# -*- coding = utf-8 -*-
# @Time : 2021/10/10 11:18
# @Author : 周孝尚
# @File : MachineLearningZoom.py
# @Software : PyCharm
import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
scale = StandardScaler()
df = pandas.read_csv('cars.csv')
X = df[['Weight', 'Volume']]
y = df['CO2']
scaledX = scale.fit_transform(X)
# print(scaledX)
regr = linear_model.LinearRegression()
regr.fit(scaledX,y)
scaled = scale.fit_transform([[2300, 1.3]])
predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)