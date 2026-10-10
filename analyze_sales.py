from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("sales_data.csv")
OUTPUT_DIR = Path(__file__).with_name("output")
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE, parse_dates=["order_date"])
df = df.drop_duplicates().dropna()
df = df[(df["quantity"] > 0) & (df["unit_price_inr"] >= 0) & (df["unit_cost_inr"] >= 0)]
df["revenue_inr"] = df["quantity"] * df["unit_price_inr"]
df["cost_inr"] = df["quantity"] * df["unit_cost_inr"]
df["profit_inr"] = df["revenue_inr"] - df["cost_inr"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

revenue = df["revenue_inr"].sum()
profit = df["profit_inr"].sum()
summary = pd.DataFrame([
    ["Total revenue (INR)", revenue],
    ["Total cost (INR)", df["cost_inr"].sum()],
    ["Total profit (INR)", profit],
    ["Profit margin (%)", round(profit / revenue * 100, 2) if revenue else 0],
    ["Units sold", df["quantity"].sum()],
    ["Order rows", len(df)]
], columns=["metric", "value"])
summary.to_csv(OUTPUT_DIR / "summary_metrics.csv", index=False)

monthly = df.groupby("month", as_index=False).agg(revenue_inr=("revenue_inr","sum"), profit_inr=("profit_inr","sum"), units_sold=("quantity","sum"))
category = df.groupby("category", as_index=False).agg(revenue_inr=("revenue_inr","sum"), profit_inr=("profit_inr","sum"), units_sold=("quantity","sum")).sort_values("revenue_inr", ascending=False)
region = df.groupby("region", as_index=False).agg(revenue_inr=("revenue_inr","sum"), profit_inr=("profit_inr","sum"), units_sold=("quantity","sum")).sort_values("revenue_inr", ascending=False)
for name, table in [("monthly_performance.csv",monthly),("category_performance.csv",category),("region_performance.csv",region)]:
    table.to_csv(OUTPUT_DIR / name, index=False)
df.to_csv(OUTPUT_DIR / "cleaned_sales_data.csv", index=False)

plt.figure(figsize=(9,5))
plt.plot(monthly["month"], monthly["revenue_inr"], marker="o")
plt.title("Monthly Revenue"); plt.xlabel("Month"); plt.ylabel("Revenue (INR)")
plt.xticks(rotation=35); plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_revenue.png", dpi=150); plt.close()

plt.figure(figsize=(9,5))
plt.bar(category["category"], category["revenue_inr"])
plt.title("Revenue by Category"); plt.xlabel("Category"); plt.ylabel("Revenue (INR)")
plt.xticks(rotation=20); plt.tight_layout()
plt.savefig(OUTPUT_DIR / "category_revenue.png", dpi=150); plt.close()

print("Analysis complete. Files saved in output/.")
print(summary.to_string(index=False))
print("\nRevenue by category:")
print(category.to_string(index=False))
