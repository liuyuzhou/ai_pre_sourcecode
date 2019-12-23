import pandas as pd

left = pd.DataFrame({'id': [1, 2, 3],
                     'Name': ['meng', 'zhi', 'wang'],
                     'number': ['1001', '1002', '1003']})
right = pd.DataFrame({'id': [1, 2, 3],
                      'Name': ['li', 'zhang', 'ming'],
                      'number': ['1001', '1002', '1005']})
rs_left = pd.merge(left, right, on='number', how='left')
print('Left Join结果：\n{}'.format(rs_left))

rs_right = pd.merge(left, right, on='number', how='right')
print('Right Join结果：\n{}'.format(rs_right))

rs_outer = pd.merge(left, right, on='number', how='outer')
print('Outer Join结果：\n{}'.format(rs_outer))

rs_inner = pd.merge(left, right, on='number', how='inner')
print('Inner Join结果：\n{}'.format(rs_inner))
