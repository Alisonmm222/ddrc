import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/land_prices.csv", sep=';', encoding='utf-8-sig')
df = read_csv("data/processed/economy.csv")

# clean data
df_nb["Gemeinde"] = df_nb["Raumeinheit"]
df_nb["Baulandpreise"] = (df_nb["Baulandpreise"]
                          .str.replace(".", "", regex=False)
                          .str.replace(",", ".", regex=False)
                          .astype(float))
# merge the two Datasets
df = df.merge(
    df_nb[["Gemeinde", "Baulandpreise"]], on="Gemeinde", how="inner")

df = df.sort_values("Stimmenanteile AfD", ascending=False)
df.dropna(inplace=True)

# Plot
x = np.arange(len(df))
width = 0.35
fig, ax1= plt.subplots(figsize=(10,6))

# AfD bars on primary y-axis
ax1.bar(x - width/2, df["Stimmenanteile AfD"], width, color="#009EE0", label="AfD %")
ax1.set_xticks(x)
ax1.set_xticklabels(df["Gemeinde"], rotation=35, ha="right", fontsize=14)
ax1.set_ylim(0, 40)
ax1.set_yticks([0, 10, 20, 30])
ax1.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:.0f} %'))

# land prices on secondary y-axis
ax2 = ax1.twinx()
ax2.bar(x + width/2, df["Baulandpreise"], width, color="#FFC422", label="Baulandpreise in qm")
ax2.set_ylim(0, max(df["Baulandpreise"])*1.1)
ax2.set_yticks([0, 400, 800, 1200])
ax2.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:.0f} €'))

# combine legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
leg = ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", fontsize=14)
leg.set_frame_on(False)
plt.title("Stimmenanteile AfD  vs Baulandpreise pro qm", fontsize=26)

# remove spines from both axes
for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_visible(False)
plt.savefig("plots/land_prices.png", dpi=300)
plt.tight_layout()
plt.show()