import pandas as pd

print("================================")
print("FINAL F1 PROJECT FINDINGS")
print("================================")

# Load final data
performance = pd.read_csv("f1_multiteam_performance.csv")
technical = pd.read_csv("18_quantitative_technical_changes.csv")

# McLaren data
mclaren = performance[
    performance["Team"] == "McLaren"
].sort_values("Season")

mclaren_2024 = mclaren[mclaren["Season"] == 2024].iloc[0]
mclaren_2025 = mclaren[mclaren["Season"] == 2025].iloc[0]

points_change = (
    mclaren_2025["Points"] - mclaren_2024["Points"]
)

wins_change = (
    mclaren_2025["Wins"] - mclaren_2024["Wins"]
)

points_percent = (
    points_change / mclaren_2024["Points"]
) * 100

wins_percent = (
    wins_change / mclaren_2024["Wins"]
) * 100


# =================================
# FINDINGS
# =================================

findings = [

    "McLaren remained 1st in the constructors' championship "
    "in both 2024 and 2025.",

    f"McLaren championship points increased from "
    f"{int(mclaren_2024['Points'])} to "
    f"{int(mclaren_2025['Points'])}, "
    f"an increase of {points_percent:.2f}%.",

    f"McLaren race wins increased from "
    f"{int(mclaren_2024['Wins'])} to "
    f"{int(mclaren_2025['Wins'])}, "
    f"an increase of {wins_percent:.2f}%.",

    "The extracted vehicle weight increased from "
    "798 kg to 800 kg.",

    "MGU-K and MGU-H were available as numerical "
    "technical specifications in the 2025 data but "
    "were not available in the 2024 extracted data.",

    "Other common numerical technical specifications "
    "showed no measurable change between the two seasons.",

    "The available data indicates an association between "
    "the observed technical data and performance improvement.",

    "The analysis does not prove that a particular "
    "technical change caused the performance improvement.",

    "More seasons, more teams, and additional technical "
    "variables would be required for stronger statistical analysis."
]


# =================================
# DISPLAY FINDINGS
# =================================

print("\n================================")
print("KEY FINDINGS")
print("================================")

for i, finding in enumerate(findings, 1):
    print(f"{i}. {finding}")


# =================================
# SAVE FINDINGS
# =================================

findings_df = pd.DataFrame({
    "Finding_No": range(1, len(findings) + 1),
    "Finding": findings
})

findings_df.to_csv(
    "21_final_findings.csv",
    index=False
)

print("\nFinal findings saved:")
print("21_final_findings.csv")


# =================================
# FINAL CONCLUSION
# =================================

conclusion = (
    "The project successfully demonstrates a web-based approach "
    "for collecting Formula 1 technical specification and "
    "performance data. The analysis shows that McLaren's "
    "performance improved substantially from 2024 to 2025, "
    "with championship points increasing by 25.08% and race "
    "wins increasing by 133.33%. At the same time, only a "
    "limited number of extracted numerical technical "
    "specifications changed. Therefore, the results identify "
    "an observed relationship between the available technical "
    "data and racing performance, but they do not establish "
    "causation. A larger dataset containing more teams, "
    "seasons, and technical variables would provide a stronger "
    "basis for statistical analysis."
)

print("\n================================")
print("PROJECT CONCLUSION")
print("================================")

print(conclusion)


# =================================
# SAVE CONCLUSION
# =================================

with open(
    "21_project_conclusion.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(conclusion)

print("\nConclusion saved:")
print("21_project_conclusion.txt")

print("\n================================")
print("STEP 21 COMPLETED")
print("================================")