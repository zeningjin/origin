import numpy as np
import matplotlib.pyplot as plt
###线性回归
# x = [1,2,3,4]
# y = [3,5,7,10] # 10, not 9, so the fit isn't perfect
#
xfit = np.polyfit(x,y,1)
# fit_fn = np.poly1d(fit)
# # fit_fn is now a function which takes in x and returns an estimate for y
#
# plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
# plt.xlim(0, 5)
# plt.ylim(0, 12)
# plt.show()

#逻辑回归
# import math
#
# def sigmoid(x):
#     a = []
#     for item in x:
#         a.append(1 / (1 + math.exp(-item)))
#     return a
# x = np.arange(-10., 10., 0.2)
# sig = sigmoid(x)
# ax = plt.gca()
# print(ax.spines['top'].set_color('none'))
# print(ax.spines['right'].set_color('none'))
# ax.spines['left'].set_position(('data',0))
# ax.spines['bottom'].set_position(('axes',0.5))
# plt.plot(x, sig)
# plt.show()

