from itertools import product
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw_sales.csv")


df["date"] = pd.to_datetime(df["date"])
df["month"]= df["date"].dt.to_period("M")               # adding month column for monthly analysis 


print("-------------ORGINAL DATA--------------")


print(df)
df = df.drop_duplicates()                            # Remove duplicates

df["price"] = pd.to_numeric(df["price"])
df["quantity"]= pd.to_numeric(df["quantity"])
df["total_sales"]= df["price"] * df["quantity"]


print("---------------CLEANED DATA--------------")


print(df)

df.to_csv("data/cleaned_sales.csv", index=False)
print("\n Cleaned file saved as data/cleaned_sales.csv")


print("\n------------SUMMARY STATISTICS----------")


total_revenue = df["total_sales"].sum()
total_orders = df["order_id"].nunique()
total_quantity = df["quantity"].sum()

print("Total_revenue:", total_revenue)
print("Total_orders:", total_orders)
print("Total_quantity:", total_quantity)


print("\n-----------CATEGORY WISE SALES-------------")


category_sales = df.groupby("category")["total_sales"].sum()
print(category_sales)


print("\n---------------BEST SELLING PRODUCTS-------------")


product_sales = df.groupby("product")["total_sales"].sum()
print(product_sales)

best_product = product_sales.idxmax()
best_product_values = product_sales.max()

print("\nTop Product:", best_product)
print("Sales Values:", best_product_values)

print("\n-------------MONTHLY SALES TRENDS-------------")


monthly_sales = df.groupby("month")["total_sales"].sum()
print(monthly_sales)

category_sales.plot(kind="bar")
plt.title("category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.savefig("outputs/category_sales.png")
plt.show()

monthly_sales.plot(kind="bar")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.savefig("outputs/monthly_sales.png")  # Save the plot as an image file
plt.show()