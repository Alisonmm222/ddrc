import pandas as pd

df = pd.read_csv("data/processed/Niederbayern Wahlergebnisse.csv")

df = df.drop(columns=["Aggregat", "Kennziffer"])

cols_to_conv = [col for col in df.columns if col != "Gemeinde"]

for c in cols_to_conv:
    df[c] = (df[c]
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float))
