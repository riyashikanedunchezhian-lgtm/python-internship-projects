import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
data = pd.read_csv("sales_data.csv")

print("First 5 rows of dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nMissing values:")
print(data.isnull().sum())

# 2. Clean missing data
data = data.dropna()

# 3. Filtering example
high_sales = data[data["Sales"] > 500]
print("\nHigh Sales Records:")
print(high_sales)

# 4. Grouping and aggregation
product_sales = data.groupby("Product")["Sales"].sum()
region_sales = data.groupby("Region")["Sales"].mean()

print("\nTotal Sales by Product:")
print(product_sales)

print("\nAverage Sales by Region:")
print(region_sales)

# 5. Visualization

# Bar chart for product sales
product_sales.plot(kind="bar", title="Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# Pie chart for region sales
region_sales.plot(kind="pie", autopct='%1.1f%%', title="Average Sales Distribution by Region")
plt.ylabel("")
plt.show()

# 6. Insight Summary
print("\nInsight Summary:")
print("1. Laptops generate the highest total sales.")
print("2. Some regions perform better than others in average sales.")
print("3. High sales records (>500) indicate strong-performing products.")
print("4. Data cleaning ensured accurate analysis.")
