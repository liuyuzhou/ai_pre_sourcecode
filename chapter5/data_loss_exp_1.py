import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 3),
                  index=['a', 'c', 'e'], columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e'])
print(df)
