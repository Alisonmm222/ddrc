from pandas import read_csv
import matplotlib.pyplot as plt

df = read_csv("processed/Niederbayern Wahlergebnisse.csv")
df = df.drop(columns=["Aggregat", "Kennziffer", "Raumeinheit"])

for c in df.columns:
    df[c] = (df[c]
                .str.replace(".", "", regex=False)
                .str.replace(",", ".", regex=False)
                .astype(float))

parties = df.iloc[0].tolist()   # first row = party names
shares = df.iloc[2].tolist()    # third row = percentages

# Convert shares to float (replace commas)
shares = [float(s.replace(",", ".")) for s in shares]

# Create DataFrame
df_plot = pd.DataFrame({
    "Party": parties,
    "Share": shares
})

# German party colors
colors = {
    "CDU/CSU": "#000000",
    "SPD": "#E3000F",
    "Grüne": "#00A551",
    "FDP": "#FFED00",
    "AfD": "#009EE0",
    "Linke": "#BE3075"
}

# Plot
plt.figure(figsize=(8,6))
plt.bar(df_plot["Party"], df_plot["Share"], color=[colors.get(p, "#AAAAAA") for p in df_plot["Party"]])
plt.ylabel("Prozent")
plt.title("Parteien in Deutschland 2025", fontsize=18)
plt.ylim(0, max(df_plot["Share"])*1.2)

# Show values on top
for i, val in enumerate(df_plot["Share"]):
    plt.text(i, val + 0.5, f"{val:.1f}%", ha="center")

plt.tight_layout()
plt.savefig("plots/wahlergebnisse.png", dpi=300)
plt.show()