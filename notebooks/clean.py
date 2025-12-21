import pandas as pd
import matplotlib.pyplot as plt

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

# Plotting Data
df_nb.plot(x = "Asylbewerber", y = "Stimmenanteile AfD", kind = "bar", title = "Stimmenanteile AfD in den Landkreisen Niederbayerns")
plt.show()

df_nb.plot(x = "Gemeinde", y = "Ausländeranteil", kind = "hist", title = "Ausländeranteil in den Landkreisen Niederbayerns")

plt.figure(figsize=(12,8))
plt.bar(df_nb["Gemeinde"], df_nb["Stimmenanteile AfD"], color='skyblue')
plt.xlabel("Gemeinde")
plt.ylabel("Stimmanteile AfD")
plt.title("Stimmanteile in den Landkreisen Niederbayerns")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

print(df_nb.info())