import matplotlib.pyplot as plt

line1, = plt.plot([1, 2, 3], label="Line 1", linestyle='--')
line2, = plt.plot([3, 2, 1], label="Line 2", linewidth=4)

# 为第一个线条创建图例
first_legend = plt.legend(handles=[line1], loc=1)
# 手动将图例添加到当前轴域
ax = plt.gca().add_artist(first_legend)

# 为第二个线条创建另一个图例
plt.legend(handles=[line2], loc=4)
plt.show()
