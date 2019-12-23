import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(5))
ts[2:-1] = np.nan
sts = ts.to_sparse()
print(sts)
