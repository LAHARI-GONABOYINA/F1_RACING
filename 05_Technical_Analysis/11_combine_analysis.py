import pandas as pd


print("================================")
print("FINAL DATA INTEGRATION")
print("================================")


# =========================================================
# 1. LOAD DATA
# =========================================================

specs = pd.read_csv("f1_specs_numeric_only.csv")
performance = pd.read_csv("f1_performance_raw.csv")
wins = pd.read_csv("f1_team_wins.csv")


print("\nTechnical specifications loaded:", len(specs))
print("Performance data loaded:", len(performance))
print("Wins data loaded:", len(wins))


# =========================================================
# 2. KEEP McLAREN DATA
# =========================================================

mclaren_specs = specs[
    specs["Team"].str.contains(
        "McLaren",
        case=False,
        na=False
    )
].copy()


mclaren_performance = performance[
    performance["Team"].str.contains(
        "McLaren",
        case=False,
        na=False
    )
].copy()


mclaren_wins = wins[
    wins["Team"].str.contains(
        "McLaren",
        case=False,
        na=False
    )
].copy()


# =========================================================
# 3. STANDARDIZE TEAM NAME
# =========================================================

mclaren_specs["Team"] = "McLaren"
mclaren_performance["Team"] = "McLaren"
mclaren_wins["Team"] = "McLaren"


# =========================================================
# 4. CREATE TECHNICAL FEATURE TABLE
# =========================================================

technical = mclaren_specs.pivot_table(
    index=["Season", "Team", "Car"],
    columns="Specification",
    values="Numeric_Value",
    aggfunc="first"
).reset_index()


technical.columns.name = None


# =========================================================
# 5. CONVERT NUMERICAL COLUMNS
# =========================================================

numeric_columns = [
    "Weight",
    "Capacity",
    "Bank angle",
    "No of valves",
    "Max speed",
    "Max fuel flow rate",
    "Fuel injection",
    "Race wheels",
    "Minimum weight",
    "MGU-K",
    "MGU-H"
]


for column in numeric_columns:

    if column in technical.columns:

        technical[column] = pd.to_numeric(
            technical[column],
            errors="coerce"
        )


# =========================================================
# 6. MERGE PERFORMANCE
# =========================================================

final_data = pd.merge(
    technical,
    mclaren_performance[
        ["Season", "Team", "Position", "Points"]
    ],
    on=["Season", "Team"],
    how="left"
)


# =========================================================
# 7. MERGE WINS
# =========================================================

final_data = pd.merge(
    final_data,
    mclaren_wins[
        ["Season", "Team", "Wins"]
    ],
    on=["Season", "Team"],
    how="left"
)


# =========================================================
# 8. CONVERT PERFORMANCE VALUES
# =========================================================

final_data["Position"] = pd.to_numeric(
    final_data["Position"],
    errors="coerce"
)

final_data["Points"] = pd.to_numeric(
    final_data["Points"],
    errors="coerce"
)

final_data["Wins"] = pd.to_numeric(
    final_data["Wins"],
    errors="coerce"
).fillna(0)


# =========================================================
# 9. SORT
# =========================================================

final_data = final_data.sort_values(
    "Season"
).reset_index(drop=True)


# =========================================================
# 10. DISPLAY FINAL DATASET
# =========================================================

print("\n================================")
print("FINAL ANALYSIS DATASET")
print("================================")

print(
    final_data.to_string(index=False)
)


# =========================================================
# 11. SAVE FINAL DATASET
# =========================================================

final_data.to_csv(
    "f1_final_mclaren_analysis.csv",
    index=False
)


# =========================================================
# 12. YEAR-TO-YEAR ANALYSIS
# =========================================================

print("\n================================")
print("2024 → 2025 PERFORMANCE CHANGE")
print("================================")


if len(final_data) >= 2:

    first = final_data.iloc[0]
    second = final_data.iloc[1]


    # -----------------------------------------------------
    # Points
    # -----------------------------------------------------

    points_change = (
        second["Points"] - first["Points"]
    )

    print(
        f"\nPoints: {first['Points']} → "
        f"{second['Points']}"
    )

    print(
        f"Points change: {points_change:+.0f}"
    )


    # -----------------------------------------------------
    # Wins
    # -----------------------------------------------------

    wins_change = (
        second["Wins"] - first["Wins"]
    )

    print(
        f"\nWins: {first['Wins']} → "
        f"{second['Wins']}"
    )

    print(
        f"Wins change: {wins_change:+.0f}"
    )


    # -----------------------------------------------------
    # Championship position
    # -----------------------------------------------------

    print(
        f"\nChampionship position: "
        f"{first['Position']:.0f} → "
        f"{second['Position']:.0f}"
    )


    # -----------------------------------------------------
    # Weight
    # -----------------------------------------------------

    if (
        pd.notna(first["Weight"])
        and pd.notna(second["Weight"])
    ):

        weight_change = (
            second["Weight"] - first["Weight"]
        )

        print(
            f"\nWeight: "
            f"{first['Weight']:.1f} kg → "
            f"{second['Weight']:.1f} kg"
        )

        print(
            f"Weight change: "
            f"{weight_change:+.1f} kg"
        )


    # -----------------------------------------------------
    # Other technical specifications
    # -----------------------------------------------------

    print("\n================================")
    print("TECHNICAL CHANGES")
    print("================================")


    compare_columns = [
        "Capacity",
        "Bank angle",
        "No of valves",
        "Max speed",
        "Max fuel flow rate",
        "Fuel injection",
        "Race wheels",
        "Minimum weight",
        "MGU-K",
        "MGU-H"
    ]


    for column in compare_columns:

        if column in final_data.columns:

            value1 = first[column]
            value2 = second[column]

            if pd.notna(value1) and pd.notna(value2):

                if value1 != value2:

                    print(
                        f"{column}: "
                        f"{value1} → {value2}"
                    )

                else:

                    print(
                        f"{column}: "
                        f"{value1} → {value2} "
                        "(No change)"
                    )


# =========================================================
# 13. FINAL MESSAGE
# =========================================================

print("\n================================")
print("DATA INTEGRATION COMPLETED")
print("================================")

print(
    "\nFinal file created:"
)

print(
    "f1_final_mclaren_analysis.csv"
)

print(
    "\nThis dataset is ready for performance analysis."
)