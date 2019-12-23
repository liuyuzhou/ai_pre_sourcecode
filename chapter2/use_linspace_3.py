import numpy as np

# 默认包含endpoint
df_np = np.linspace(10, 20, 5)
print(df_np)

# 设置endpoint为False
df_np = np.linspace(10, 20, 5, endpoint=False)
print(df_np)

# 默认包含endpoint
end_np = np.linspace(10, 20, 5, dtype=int)
print(end_np)

int_np = np.linspace(10, 20, 5, endpoint=False, dtype=int)
print(int_np)
