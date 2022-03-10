import plotly
import plotly.graph_objects as go
import datetime

import pandas as pd
from pyparsing import AtLineStart

from sklearn.neighbors import LocalOutlierFactor
from sqlalchemy import column
# ==============================================================================
# ==============================================================================
# ==============================================================================
# 讀綁案
# read_data = pd.read_excel('data_1228_1.xlsx')
read_data = pd.read_excel('data_1228_1.xlsx')
y_header = read_data.columns.values
print('讀綁案')
print(read_data)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# LOF 演算法
test_data = [[1],[1],[1],[1],[10],[1],[1],[1],[1],[1]]
clf = LocalOutlierFactor(n_neighbors=2,metric='manhattan')
clf.fit_predict(test_data)
factor = abs(clf.negative_outlier_factor_)
print('factor')
print(factor)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# 設備時間(格式為datetime時間格式)
alist = []
blist = []
clist = []
for x in range(0, 419):
    alist.append(read_data.loc[x, 'time'])
x_data = alist
# x_data = [ read_data.loc[0,'time'],read_data.loc[1,'time'],read_data.loc[2,'time'],read_data.loc[3,'time'],read_data.loc[4,'time'],read_data.loc[5,'time'] ]
# 設備名稱
for y in range(1, 277):
    blist.append(y_header[y])
print("clist")
# print(blist)
y_data = blist
# y_data = ['sm23-2_6', 'sm23-2_5', 'sm23-2_4', 'sm23-2_3', 'sm23-2_2', 'sm23-2_1']
# 設備的數據
for z in range(1,277) :
    clist.append(read_data[ y_header[z]])
z_data = clist
print(z_data)
# z_data = [ [1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,4,5,6],[7,8,9,10,11,12],[1,2,3,4,5,6],[7,8,9,10,11,12] ]


fig = go.Figure(data=go.Heatmap(
        z= z_data,
        x= x_data,
        y= y_data,))

fig.update_layout(
    title='標題',
    xaxis_nticks=36)
plotly.offline.plot(fig, filename = 'result.html', auto_open = True) # True False
# ==============================================================================
# ==============================================================================
# ==============================================================================