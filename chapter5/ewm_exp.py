import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6, 4),
                  index=pd.date_range('1/1/2019', periods=6),
                  columns=['A', 'B', 'C', 'D'])
print(df.ewm(com=0.5).mean())
