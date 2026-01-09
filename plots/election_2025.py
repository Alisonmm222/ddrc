import pandas as pd
import sys
from pathlib import Path
import os
print(os.getcwd())

#file_path = Path(__file__).parent / "processed" / "Niederbayern Wahlergebnisse.csv"
#df = pd.read_csv(file_path)
print(os.getcwd())

df = pd.read_csv("/processed/Niederbayern Wahlergebnisse.csv")

df = df.drop(columns=["Aggregat", "Kennziffer", "Raumeinheit"])

for c in df.columns:
    df[c] = (df[c]
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float))
