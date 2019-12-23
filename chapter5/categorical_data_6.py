import pandas as pd

sr = pd.Series(["a", "b", "c", "a"], dtype="category")
print("初始对象:\n{}".format(sr))
sr = sr.cat.add_categories([4])
print('追加新类别后的对象：\n{}'.format(sr.cat.categories))
print('删除指定类别后的对象：\n{}'.format(sr.cat.remove_categories("a")))
