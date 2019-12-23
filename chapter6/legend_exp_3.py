import matplotlib.lines as m_lines
import matplotlib.pyplot as plt

blue_line = m_lines.Line2D([], [], color='blue', marker='*',
                           markersize=15, label='Blue stars')
plt.legend(handles=[blue_line])
plt.show()
