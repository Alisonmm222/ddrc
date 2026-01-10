import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/economy.csv")

df_nb = df_nb.sort_values("Stimmenanteile AfD", ascending=False)

# unemployment rate across Germany for baseline
gesamt_alq_ausl = 37.08 # 2023 INKAR

# Plot
x = np.arange(len(df_nb["Gemeinde"])) * 1.4
width = 0.4

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD %", color = "#009EE0")
plt.bar(x + 0.5*width, df_nb["Ausländische Arbeitslose"], width, color="#F25A7D", label="Ausländische Arbeitslose %")

# unemployment baseline
plt.axhline(y=gesamt_alq_ausl, color="#F25A7D", linestyle="--", linewidth=2, label = "deutschlandweit")

# remove the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])
plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=14, ha = "right")

plt.legend(edgecolor="none", fontsize=14)
plt.title("Stimmenanteile AfD vs Ausländische AL", fontsize=26)
plt.tight_layout()
plt.savefig('plots/unemployment.png', dpi=300)
plt.show()