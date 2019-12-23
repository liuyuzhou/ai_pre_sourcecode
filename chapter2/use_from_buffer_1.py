import numpy as np

pri_str = b'Hello World'
fb_np = np.frombuffer(pri_str, dtype='S1')
print(fb_np)
