import matplotlib.pyplot as plt
from pandas import read_csv
import numpy as np

df_nb = read_csv("data/processed/Tabelle Migration.csv")

df_nb = df_nb.sort_values("Stimmenanteile AfD", ascending=False)

# Asylsuchende und Schutzsuchende
gesamt_asyl = 5.97  # 2023 INKAR

x = np.arange(len(df_nb["Gemeinde"])) * 1.2
width = 0.5

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD", color = "#009EE0")
plt.bar(x + 0.5*width, df_nb["Asylbewerber"], width, color="#B7E4C7", label="Asylbewerber")
# Germany baseline
plt.axhline(y=gesamt_asyl, color="#B7E4C7", linestyle="--", linewidth=2, label="Deutschland")
plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=11, ha = "right")
plt.legend()
plt.title("Stimmanteile AfD und Asylbewerber", fontsize=18)
plt.tight_layout()
plt.savefig('plots/asyl.png', dpi=300)
plt.show()


# Ausländeranteil
gesamt_ausl = 14.51 # 2023 INKAR

x = np.arange(len(df_nb["Gemeinde"])) * 1.2
width = 0.5

plt.figure(figsize=(10,6))
plt.bar(x - width/2, df_nb["Stimmenanteile AfD"], width, label="AfD", color = "#009EE0")
plt.bar(x + width/2, df_nb["Ausländeranteil"], width, color="#D8BFD8", label="Ausländeranteil")
# Germany baseline
plt.axhline(y=gesamt_ausl, color="#E6CCE6", linestyle="--", linewidth=2, label="Deutschland")
plt.xticks( ticks=x, labels=df_nb["Gemeinde"], rotation=35, fontsize=11, ha = "right")
plt.legend()
plt.title("Stimmanteile in den Landkreisen Niederbayerns")
plt.tight_layout()
plt.savefig('plots/foreigners.png', dpi=300)
plt.show()






