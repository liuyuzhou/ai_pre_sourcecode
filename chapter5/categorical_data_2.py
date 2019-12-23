import pandas as pd

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print('示例一：\n{}'.format(cat))

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'])
print('示例二：\n{}'.format(cat))

cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c', 'd'], ['c', 'b', 'a'], ordered=True)
print('示例三：\n{}'.format(cat))
