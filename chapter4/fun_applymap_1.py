import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
df['col1'].map(lambda x: x*100)
print(df)
