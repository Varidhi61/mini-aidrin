import pandas as pd
from loaders.base_loader import BaseLoader

class CSVLoader(BaseLoader):
    def load(self, path):
        print("📂 Loading CSV file...")
        return pd.read_csv(path)