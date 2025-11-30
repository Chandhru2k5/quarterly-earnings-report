# 23f3001440@ds.study.iitm.ac.in
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------------------------------------
# Generate synthetic business data
# -----------------------------------------------------------
data = {
    "Product_Category": [
        "Electronics", "Furniture", "Groceries",
        "Clothing", "Beauty", "Sports"
    ],
    "Avg_Satisfaction": [4.2, 3.8, 4.5, 3.9, 4.1, 4.3]
}
df = pd.DataFrame(data)

# -----------------------------------------------------------
# Professional Seaborn styling
# -----------------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 8))  # 512x512 px because DPI = 64 below

ax = sns.barplot(
    data=df,
    x="Product_Category",
    y="Avg_Satisfaction",
    palette="Blues_d"
)

ax.set_title("Customer Satisfaction by Product Category", fontsize=18)
ax.set_xlabel("Product Category", fontsize=14)
ax.set_ylabel("Average Satisfaction Score", fontsize=14)
plt.xticks(rotation=20)

# -----------------------------------------------------------
# Save chart with EXACT dimensions 512x512
# -----------------------------------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")  # 8 * 64 = 512 px
