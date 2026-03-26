import h5py
import numpy as np

# use np.nan for missing
data = np.array([
    [25, 50000, 0],
    [30, np.nan, 1],   # 👈 missing value
    [22, 45000, 0]
], dtype=float)

with h5py.File("test.h5", "w") as f:
    f.create_dataset("data", data=data)

print("✅ test.h5 file created")