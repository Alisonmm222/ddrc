# Plotting Data migration and AfD votes in Lower Bavaria
import matplotlib.pyplot as plt

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

