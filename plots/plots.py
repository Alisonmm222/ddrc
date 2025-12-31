# Plotting Data migration and AfD votes in Lower Bavaria
import matplotlib.pyplot as plt
from pandas import read_csv

df_nb = read_csv("data/processed/Tabelle Migration.csv")

df_nb.plot(x = "Asylbewerber", y = "Stimmenanteile AfD", kind = "bar", title = "Stimmenanteile AfD in den Landkreisen Niederbayerns")
plt.savefig('plots/figures/afd_votes_lower_bavaria.png', dpi=150)
plt.show()

df_nb.plot(x = "Gemeinde", y = "Ausländeranteil", kind = "hist", title = "Ausländeranteil in den Landkreisen Niederbayerns")
plt.savefig('figures/afd_votes_lower_bavaria.png', dpi=150)
plt.show()

plt.figure(figsize=(12,8))
plt.bar(df_nb["Gemeinde"], df_nb["Stimmenanteile AfD"], color='skyblue')
plt.xlabel("Gemeinde")
plt.ylabel("Stimmanteile AfD")
plt.title("Stimmanteile in den Landkreisen Niederbayerns")
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('plots/figures/afd_votes_lower_bavaria.png', dpi=150)
plt.show()

print(df_nb.info())

