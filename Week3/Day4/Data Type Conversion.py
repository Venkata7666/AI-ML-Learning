import pandas as pd
df = pd.DataFrame(
    {
        "price": ["10.50", "25.00", "7.99"],
        "quantity": ["2", "4", "1"],
        "order_date": ["2024-01-15", "2024-02-20", "2024-03-05"],
        "status": ["Pending", "Completed", "Pending"],
    }
)

df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype("Int64")

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

df["status"] = df["status"].astype("category")

print(df)
print(df.dtypes)