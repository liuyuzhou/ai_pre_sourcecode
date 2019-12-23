import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4, 3), columns=['col1', 'col2', 'col3'])
for key, value in df.iteritems():
    print(key, value)
