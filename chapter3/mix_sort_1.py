import numpy as np

# 复数排序
print('复数排序:{}'.format(np.sort_complex([5, 3, 6, 2, 1])))
print('复数排序:{}'.format(np.sort_complex([1 + 2j, 2 - 1j, 3 - 2j, 3 - 3j, 3 + 5j])))

# 分区排序
num_np = np.array([3, 4, 2, 1])
# 将数组num_np中所有元素（包括重复元素）从小到大排列，比第3小的放在前面，大的放在后面
print('分区排序:{}'.format(np.partition(num_np, 3)))
# 小于1的在前面，大于3的在后面，1和3之间的在中间
print('分区排序:{}'.format(np.partition(num_np, (1, 3))))

# 找到数组的第 3 小（index=2）的值和第 2 大（index=-2）的值
arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
print('初始数组：{}'.format(arr))
print('找到数组的第3小的值：{}'.format(arr[np.argpartition(arr, 2)[2]]))
print('找到数组的第2大的值：{}'.format(arr[np.argpartition(arr, -2)[-2]]))

# 同时找到第3和第4小的值。用[2,3]同时将第3和第4小的排序好，然后可以分别通过下标[2]和[3]取得。
print('找到数组的第3小的值：{}'.format(arr[np.argpartition(arr, [2, 3])[2]]))
print('找到数组的第4小的值：{}'.format(arr[np.argpartition(arr, [2, 3])[3]]))




