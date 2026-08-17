import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

# Load datasets
customers = pd.read_csv(DATA_PATH / "customers.csv")
restaurants = pd.read_csv(DATA_PATH / "restaurants.csv")
drivers = pd.read_csv(DATA_PATH / "drivers.csv")
orders = pd.read_csv(DATA_PATH / "orders.csv")
deliveries = pd.read_csv(DATA_PATH / "deliveries.csv")
reviews = pd.read_csv(DATA_PATH / "reviews.csv")
payments = pd.read_csv(DATA_PATH / "payments.csv")


# -----------------------------
# 1. Row counts
# -----------------------------

datasets = {
    "Customers": customers,
    "Restaurants": restaurants,
    "Drivers": drivers,
    "Orders": orders,
    "Deliveries": deliveries,
    "Reviews": reviews,
    "Payments": payments
}

print("\n========== ROW COUNTS ==========")

for name, df in datasets.items():
    print(f"{name}: {df.shape}")


# -----------------------------
# 2. Missing values
# -----------------------------

print("\n========== MISSING VALUES ==========")

for name, df in datasets.items():
    print(f"\n{name}")
    print(df.isnull().sum())


# -----------------------------
# 3. Duplicate IDs
# -----------------------------

print("\n========== DUPLICATE IDs ==========")

print("Customer IDs:",
      customers["customer_id"].duplicated().sum())

print("Restaurant IDs:",
      restaurants["restaurant_id"].duplicated().sum())

print("Driver IDs:",
      drivers["driver_id"].duplicated().sum())

print("Order IDs:",
      orders["order_id"].duplicated().sum())

print("Delivery IDs:",
      deliveries["delivery_id"].duplicated().sum())

print("Review IDs:",
      reviews["review_id"].duplicated().sum())

print("Payment IDs:",
      payments["payment_id"].duplicated().sum())


# -----------------------------
# 4. Foreign-key validation
# -----------------------------

print("\n========== FOREIGN KEY VALIDATION ==========")

invalid_order_customer = (
    ~orders["customer_id"].isin(customers["customer_id"])
).sum()

invalid_order_restaurant = (
    ~orders["restaurant_id"].isin(restaurants["restaurant_id"])
).sum()

invalid_delivery_order = (
    ~deliveries["order_id"].isin(orders["order_id"])
).sum()

invalid_delivery_driver = (
    ~deliveries["driver_id"].isin(drivers["driver_id"])
).sum()

invalid_review_order = (
    ~reviews["order_id"].isin(orders["order_id"])
).sum()

invalid_review_customer = (
    ~reviews["customer_id"].isin(customers["customer_id"])
).sum()

invalid_payment_order = (
    ~payments["order_id"].isin(orders["order_id"])
).sum()


print("Invalid customer IDs in Orders:", invalid_order_customer)
print("Invalid restaurant IDs in Orders:", invalid_order_restaurant)
print("Invalid order IDs in Deliveries:", invalid_delivery_order)
print("Invalid driver IDs in Deliveries:", invalid_delivery_driver)
print("Invalid order IDs in Reviews:", invalid_review_order)
print("Invalid customer IDs in Reviews:", invalid_review_customer)
print("Invalid order IDs in Payments:", invalid_payment_order)


print("\n========== VALIDATION COMPLETE ==========")