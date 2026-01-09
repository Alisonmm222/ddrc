import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/Wirtschaftliche Lage.csv")

df_nb = df_nb.sort_values("Stimmenanteile AfD", ascending=False)

# Arbeitslosenquote
gesamt_alq = 5.67  # 2023 INKAR
gesamt_alq_ausl = 37.08 # 2023 INKAR

x = np.arange(len(df_nb["Gemeinde"])) * 1.4
width = 0.4

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD", color = "#009EE0")
plt.bar(x + 0.5*width, df_nb["Ausländische Arbeitslose"], width, color="#BFD7EA", label="Ausländische Arbeitslose")
plt.bar(x + 1.5*width, df_nb["Arbeitslosenquote"], width, color="#FADADD", label="Arbeitslosenquote")

# Baseline Arbeitslosenquote
plt.axhline(y=gesamt_alq, color="#FADADD", linestyle="--", linewidth=2, label="Deutschland ALQ")
# Baseline Auslädnische Arbeitslosenquote
plt.axhline(y=gesamt_alq_ausl, color="#BFD7EA", linestyle="--", linewidth=2, label="Deutschland AL-Ausländer")

plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=11, ha = "right")
plt.legend()
plt.title("Stimmanteile AfD und Arbeitslosenquote", fontsize=18)
plt.tight_layout()
plt.savefig('plots/arbeitslose.png', dpi=300)
plt.show()