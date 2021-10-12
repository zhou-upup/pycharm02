# -*- coding = utf-8 -*-
# @Time : 2021/10/11 21:24
# @Author : 周孝尚
# @File : MachienLearningDecisionTree.py
# @Software : PyCharm
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import  matplotlib.image as pltimg
df = pandas.read_csv('shows02.csv')
# print(df)
'''将字符串更改为数值'''
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
# print(type(df))
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
# print(df)
features = ['Age','Experience', 'Rank', 'Nationality']
X = df[features]
y = df['Go']
# print(X)
# print(y)
# dtree = DecisionTreeClassifier()
# dtree = dtree.fit(X,y)
# data = tree.export_graphviz(dtree, out_file=None,feature_names=feathers)
# graph = pydotplus.graph_from_dot_data(data)
# graph.write_png('mydecisiontree.png')
# img = pltimg.imread('mydecisiontree.png')
# imgplot = plt.imshow(img)
# plt.show()


dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)
data = tree.export_graphviz(dtree, out_file=None, feature_names=features)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
# plt.show()
print(dtree.predict([[40,12,9,1]]))