import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(10))
ts[2:-2] = np.nan
sts = ts.to_sparse()
print(sts.to_dense())
