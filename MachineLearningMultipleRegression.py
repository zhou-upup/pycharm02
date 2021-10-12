# -*- coding = utf-8 -*-
# @Time : 2021/10/10 11:02
# @Author : 周孝尚
# @File : MachineLearningMultipleRegression.py
# @Software : PyCharm
import pandas
df = pandas.read_csv('cars.csv')
X = df[['Weight', 'Volume']]
y = df['CO2']
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X,y)
predictedCO2 = regr.predict([[2300,1300]])
print(predictedCO2)
print(regr.coef_)