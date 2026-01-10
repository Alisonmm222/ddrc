import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/migration.csv")

df_nb = df_nb.sort_values("Stimmenanteile AfD", ascending=False)

# asylum seekers rate across Germany for baseline
gesamt_asyl = 5.97  # 2023 INKAR

x = np.arange(len(df_nb["Gemeinde"])) * 1.2
width = 0.5

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD %", color = "#009EE0")
plt.bar(x + 0.5*width, df_nb["Asylbewerber"], width, color="#B7E4C7", label="Asylbewerber %")

# baseline
plt.axhline(y=gesamt_asyl, color="#B7E4C7", linestyle="--", linewidth=2, label="deutschlandweit")
plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=14, ha = "right")
plt.legend(edgecolor="none", fontsize=14)

# Remove the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])


plt.title("Stimmenanteile AfD vs Asylbewerber", fontsize=26)
plt.tight_layout()
plt.savefig('plots/asylum.png', dpi=300)
plt.show()

# percentage of foreigners basline across germany
gesamt_ausl = 14.51 # 2023 INKAR

x = np.arange(len(df_nb["Gemeinde"])) * 1.4
width = 0.5

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD %", color = "#009EE0")
plt.bar(x + width/2, df_nb["Ausländeranteil"], width, color="#9E3EED", label="Ausländeranteil %")

# baseline
plt.axhline(y=gesamt_ausl, color="#9E3EED", linestyle="--", linewidth=2, label="deutschlandweit")
plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=14, ha = "right")

plt.legend(edgecolor='none', fontsize=14)
plt.title("Stimmenanteile AfD vs Ausländeranteil", fontsize=26)
plt.tight_layout()

# remove the frame
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.yticks([])
plt.savefig('plots/foreigners.png', dpi=300)
plt.show()