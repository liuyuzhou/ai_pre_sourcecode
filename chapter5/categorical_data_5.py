import pandas as pd

sr = pd.Series(["a", "b", "c", "a"], dtype="category")
sr.cat.categories = ["Group %s" % g for g in sr.cat.categories]

print(sr.cat.categories)
