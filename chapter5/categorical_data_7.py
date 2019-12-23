import pandas as pd

cat_1 = pd.Series([1, 2, 3]).astype("category", categories=[1, 2, 3], ordered=True)
cat_2 = pd.Series([2, 2, 2]).astype("category", categories=[1, 2, 3], ordered=True)
print(cat_1 > cat_2)
