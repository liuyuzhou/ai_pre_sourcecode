import pandas as pd
import numpy as np

sr_pd = pd.Series(np.random.np.random.randn(4), index=list('abcd'))
sr_pd['d'] = sr_pd['b']
print(sr_pd.rank())
