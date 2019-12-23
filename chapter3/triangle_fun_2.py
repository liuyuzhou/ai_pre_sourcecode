import numpy as np

angle_num = np.array([0, 30, 45, 60, 90])
sin = np.sin(angle_num * np.pi / 180)
print('数组中各个角度的正弦值：\n{}'.format(sin))

inv = np.arcsin(sin)
print('各个角度的反正弦，返回值以弧度为单位：\n{}'.format(inv))
print('通过转化为角度制来检查结果：\n{}'.format(np.degrees(inv)))

cos = np.cos(angle_num * np.pi / 180)
print('数组中各个角度的余弦值：\n{}'.format(cos))

inv = np.arccos(cos)
print('各个角度的反余弦值：\n{}'.format(inv))
print('各个角度的角度制单位：\n{}'.format(np.degrees(inv)))

tan = np.tan(angle_num * np.pi / 180)
print('各个角度的正切值：\n{}'.format(tan))

inv = np.arctan(tan)
print('各个角度的反正切值：\n{}'.format(inv))

print('各个角度的角度制单位：\n{}'.format(np.degrees(inv)))
