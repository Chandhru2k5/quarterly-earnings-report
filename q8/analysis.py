import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Data Setup
# -----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Patient_Satisfaction_Score": [1.89, 3.74, 1.41, 7.64],
}

industry_target = 4.5

df = pd.DataFrame(data)

# Compute statistics
average_score = df["Patient_Satisfaction_Score"].mean()
min_score = df["Patient_Satisfaction_Score"].min()
max_score = df["Patient_Satisfaction_Score"].max()

print("=== Patient Satisfaction - 2024 Quarterly Data ===")
print(df)
print(f"\nAverage Satisfaction Score: {average_score:.2f}")
print(f"Minimum Quarterly Score: {min_score:.2f}")
print(f"Maximum Quarterly Score: {max_score:.2f}")
print(f"Industry Target: {industry_target:.2f}")
print(f"Gap to Target (Average): {industry_target - average_score:.2f}")

# -----------------------------
# 2. Visualization
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Patient_Satisfaction_Score"],
         marker="o", linewidth=2)
plt.axhline(y=industry_target, linestyle="--")

plt.title("Patient Satisfaction Score - 2024 Quarterly Trend")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")
plt.ylim(0, max(industry_target, max_score) + 1)

for x, y in zip(df["Quarter"], df["Patient_Satisfaction_Score"]:
    plt.text(x, y + 0.1, f"{y:.2f}", ha="center", va="bottom", fontsize=9)

plt.text(
    0.02, 0.02,
    f"Average: {average_score:.2f}",
    transform=plt.gca().transAxes,
    fontsize=9,
)

plt.tight_layout()
plt.savefig("patient_satisfaction_trend.png", dpi=300)
plt.close()

print("\nSaved plot as 'patient_satisfaction_trend.png'")
