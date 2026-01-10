import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/processed/election_nb.csv", encoding='utf-8-sig', sep = ";")

# clean the data manually
df = df.drop(columns=["Aggregat", "Kennziffer", "Raumeinheit"]) # delete rows
df.columns = [c.split(' ', 1)[1] for c in df.columns]
shares = df.iloc[1]  # second row = percentages
shares = [float(s.replace(",", ".")) for s in shares] # Convert shares to float (replace commas)

# create DataFrame
df_plot = pd.DataFrame({"Party": df.columns, "Share": shares})
df_plot = df_plot.sort_values("Share", ascending=False)

# german party colors
colors = {
    "CDU/CSU": "#000000",
    "SPD": "#E3000F",
    "Grüne": "#00A551",
    "FDP": "#FFED00",
    "AfD": "#009EE0",
    "Die Linke": "#BE3075"}

# Plot
plt.figure(figsize=(10,6))

# map parties to colors
bar_colors = [colors.get(party, "#888888") for party in df_plot["Party"]]

plt.bar(df_plot["Party"], df_plot["Share"], color= bar_colors)
plt.title("Wahlergebnisse Niederbayern 2025", fontsize=26)
plt.ylim(0, max(df_plot["Share"])*1.2)

# show values on top
for i, val in enumerate(df_plot["Share"]):
    plt.text(i, val + 0.5, f"{val:.1f}%", ha="center", fontsize=20)

# remove the frame and axis
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.yticks([])
plt.xticks(fontsize=14)

plt.tight_layout()
plt.savefig("plots/election_nb.png", dpi=300)
plt.show()