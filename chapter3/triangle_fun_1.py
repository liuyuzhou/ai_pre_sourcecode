import numpy as np

angle_num = np.array([0, 30, 45, 60, 90])
print('数组中各个角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(angle_num * np.pi / 180))

print('数组中各个角度的余弦值：')
print(np.cos(angle_num * np.pi / 180))

print('数组中各个角度的正切值：')
print(np.tan(angle_num * np.pi / 180))
