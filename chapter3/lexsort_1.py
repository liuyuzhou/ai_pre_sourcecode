import numpy as np

name_tp = ('meng', 'li', 'zhang', 'wang')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
lex_sort = np.lexsort((dv, name_tp))
print('调用 lexsort() 函数：{}'.format(lex_sort))

sort_rt = [name_tp[i] + ", " + dv[i] for i in lex_sort]
print('使用索引获取排序后的数据：{}'.format(sort_rt))
