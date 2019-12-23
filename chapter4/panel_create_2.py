import pandas as pd
import numpy as np

data = {'item_1': pd.DataFrame(np.random.randn(4, 3)),
        'item_2': pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
