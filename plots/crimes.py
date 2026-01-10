import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/inner_security.csv")
df_nb = df_nb.sort_values("Stimmenanteile AfD", ascending=False)

# Plot
x = np.arange(len(df_nb))
width = 0.35

fig, ax1 = plt.subplots(figsize=(10,6))

# AfD bars on primary y-axis
ax1.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, color="#009EE0", label="Stimmenanteile AfD")
ax1.set_xticks(x)
ax1.set_xticklabels(df_nb["Gemeinde"], rotation=35, ha="right", fontsize=14)
ax1.set_ylim(0, 40)
ax1.set_yticks([0, 10, 20, 30])

# crimes on secondary y-axis
ax2 = ax1.twinx()
ax2.bar(x + width/2, df_nb["Straftaten"], width, color="#FFB266", label="Straftaten je 100.000 Einwohner")
ax2.set_ylim(0, max(df_nb["Straftaten"])*1.1)  # small margin above
ax2.set_yticks([0, 4000, 8000, 12000])

# combine legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
leg = ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left", fontsize=14)
leg.set_frame_on(False)
plt.title("Stimmenanteile AfD  vs Straftaten", fontsize=26)

# remove spines from both axes
for ax in [ax1, ax2]:
    for spine in ax.spines.values():
        spine.set_visible(False)

plt.savefig("plots/crimes.png", dpi=300)
plt.tight_layout()
plt.show()