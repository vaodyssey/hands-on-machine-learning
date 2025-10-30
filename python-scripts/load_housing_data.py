import pandas as pd
import os 

def load_housing_data(housing_path):
    csv_path = os.path.join(housing_path)
    return pd.read_csv(csv_path)