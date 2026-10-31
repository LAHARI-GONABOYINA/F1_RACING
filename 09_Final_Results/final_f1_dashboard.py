import matplotlib.pyplot as plt

# ================================
# FINAL F1 DASHBOARD
# ================================

# Data
seasons = [2024, 2025]

mclaren_points = [666, 833]
mercedes_points = [468, 469]

mclaren_wins = [6, 14]
mercedes_wins = [4, 2]

# Calculate changes
points_change = mclaren_points[1] - mclaren_points[0]
points_percentage = (points_change / mclaren_points[0]) * 100

wins_change = mclaren_wins[1] - mclaren_wins[0]
wins_percentage = (wins_change / mclaren_wins[0]) * 100

# ================================
# CREATE DASHBOARD
# ================================

fig = plt.figure(figsize=(12, 8))

fig.suptitle(
    "FORMULA 1 - FINAL PROJECT DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

# --------------------------------
# Championship Points
# --------------------------------

ax1 = fig.add_axes([0.08, 0.55, 0.38, 0.30])

ax1.plot(
    seasons,
    mclaren_points,
    marker="o",
    linewidth=2,
    label="McLaren"
)

ax1.plot(
    seasons,
    mercedes_points,
    marker="o",
    linewidth=2,
    label="Mercedes"
)

ax1.set_title("Championship Points")
ax1.set_xlabel("Season")
ax1.set_ylabel("Points")

ax1.set_xticks([2024, 2025])

ax1.grid(True, alpha=0.25)
ax1.legend()

# --------------------------------
# Race Wins
# --------------------------------

ax2 = fig.add_axes([0.54, 0.55, 0.38, 0.30])

ax2.plot(
    seasons,
    mclaren_wins,
    marker="o",
    linewidth=2,
    label="McLaren"
)

ax2.plot(
    seasons,
    mercedes_wins,
    marker="o",
    linewidth=2,
    label="Mercedes"
)

ax2.set_title("Race Wins")
ax2.set_xlabel("Season")
ax2.set_ylabel("Wins")

ax2.set_xticks([2024, 2025])

ax2.grid(True, alpha=0.25)
ax2.legend()

# --------------------------------
# Key Findings
# --------------------------------

ax3 = fig.add_axes([0.08, 0.12, 0.84, 0.28])

ax3.axis("off")

metrics = [
    ("McLaren Points", "666 → 833", f"+{points_percentage:.2f}%"),
    ("McLaren Wins", "6 → 14", f"+{wins_percentage:.2f}%"),
    ("Championship Position", "1 → 1", "Maintained"),
    ("Car Weight", "798 → 800 kg", "+2 kg")
]

for i, (title, value, change) in enumerate(metrics):

    x = 0.125 + i * 0.25

    ax3.text(
        x,
        0.72,
        title,
        ha="center",
        fontsize=11,
        fontweight="bold"
    )

    ax3.text(
        x,
        0.45,
        value,
        ha="center",
        fontsize=15
    )

    ax3.text(
        x,
        0.20,
        change,
        ha="center",
        fontsize=11
    )

# ================================
# SAVE ONLY THIS DASHBOARD
# ================================

plt.savefig(
    "final_f1_dashboard.png",
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("================================")
print("FINAL DASHBOARD CREATED")
print("================================")
print("File created:")
print("final_f1_dashboard.png")