import missingno as msn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
datas=pd.read_csv(r'D:\workplace\人工智能\day11\data\adult.txt',sep=',',names=range(15))
for c in datas.columns:
    datas[c][datas[c] == ' ?'] =np.NAN
# msn.matrix(datas)
msn.heatmap(datas)
plt.show()