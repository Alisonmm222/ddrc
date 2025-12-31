import pandas as pd

df = pd.read_csv("data/raw/Tabelle Migration.csv", sep =";")

# Cleaning Data
df.dropna(inplace = True)
df_nb = df.loc[df["Raumeinheit"].isin(["Kelheim", "Straubing-Bogen", "Straubing", "Freyung-Grafenau", "Passau, Stadt", "Regen", "Deggendorf",
                                      "Dingolfing-Landau", "Landshut, Stadt", "Rottal-Inn", "Passau"])]
df_nb = df_nb.drop(columns=["Aggregat", "Kennziffer"])
df_nb = df_nb.rename(columns={"Raumeinheit": "Gemeinde"})
df_nb["Gemeinde"] = df_nb["Gemeinde"].astype("string")

cols_to_conv = [col for col in df_nb.columns if col != "Gemeinde"]
for c in cols_to_conv:
    df_nb[c] = df_nb[c].str.replace(",", ".").astype("float")



