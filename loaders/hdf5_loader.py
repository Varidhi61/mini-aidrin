
import h5py
import pandas as pd
from loaders.base_loader import BaseLoader

class HDF5Loader(BaseLoader):
    def load(self, path):
        print("📂 Loading HDF5 file...")

        with h5py.File(path, 'r') as f:
            dataset = list(f.keys())[0]
            data = f[dataset][:]

        # force correct structure
        df = pd.DataFrame(data)
        df.columns = ["age", "salary", "target"]

        print("DEBUG DF:\n", df)

        return df