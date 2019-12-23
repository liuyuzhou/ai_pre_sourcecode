import matplotlib.pyplot as plt

plt.figure(1)                # 第一个图形
plt.subplot(211)             # 第一个图形的第一个子图
plt.plot([1, 2, 3])
plt.subplot(212)             # 第一个图形的第二个子图
plt.plot([4, 5, 6])

plt.figure(2)                # 第二个图形
plt.plot([4, 5, 6])          # 默认创建 subplot(111)

plt.figure(1)                # 当前是图形 1，subplot(212)
plt.subplot(211)             # 将第一个图形的 subplot(211) 设为当前子图
plt.title('Easy as 1, 2, 3') # 子图 211 的标题
plt.show()
# plt.clf()
plt.close()
