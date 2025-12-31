import os
from dotenv import load_dotenv
from pathlib import Path
import pandas as pd
load_dotenv()

def clean_csv(input_path, output_path):
    df = pd.read_csv(input_path, sep =";")

    # Cleaning Data
    df.dropna(inplace = True)
    df_nb = df.loc[df["Raumeinheit"].isin(["Kelheim", "Straubing-Bogen", "Straubing", "Freyung-Grafenau", "Passau, Stadt", "Regen", "Deggendorf",
                                           "Dingolfing-Landau", "Landshut, Stadt", "Rottal-Inn", "Passau"])]
    df_nb = df_nb.drop(columns=["Aggregat", "Kennziffer"])
    df_nb = df_nb.rename(columns={"Raumeinheit": "Gemeinde"})
    df_nb["Gemeinde"] = df_nb["Gemeinde"].astype("string")

    cols_to_conv = [col for col in df_nb.columns if col != "Gemeinde"]

    for c in cols_to_conv:
        df_nb[c] = (df_nb[c]
                    .str.replace(".", "", regex=False)
                    .str.replace(",", ".", regex=False)
                    .astype(float))

    df_nb.to_csv(output_path, index=False)

RAW_DIR = Path(os.environ.get("RAW_DIR"))
PROCESSED_DIR = Path(os.environ.get("PROCESSED_DIR"))

for csv_file in RAW_DIR.glob("*.csv"):
    processed_df = PROCESSED_DIR/csv_file.name
    clean_csv(csv_file, processed_df)
