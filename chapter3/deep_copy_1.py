import numpy as np

a_np = np.array([[10, 10], [2, 3], [4, 5]])
print('数组a_np：\n{}'.format(a_np))

b_np = a_np.copy()
print('创建a_np的深层副本：\n{}'.format(b_np))

# b_np与a_np不共享任何内容
print('b_np与a_np是否相同：{}'.format(b_np is a_np))

b_np[0, 0] = 100
print('修改b_np的内容，修改后的数组b_np：\n{}'.format(b_np))

print('a_np保持不变：\n{}'.format(a_np))
