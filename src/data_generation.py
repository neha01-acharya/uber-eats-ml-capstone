import numpy as np
import pandas as pd
from faker import Faker

# Reproducibility
np.random.seed(42)
Faker.seed(42)

fake = Faker()

##customer dataset
# Number of customers
num_customers = 2000

customers = pd.DataFrame({
    "customer_id": [f"C{i:05d}" for i in range(1, num_customers + 1)],
    
    "age": np.random.randint(18, 65, num_customers),
    
    "gender": np.random.choice(
        ["Male", "Female", "Other"],
        size=num_customers,
        p=[0.48, 0.48, 0.04]
    ),
    
    "city": np.random.choice(
        ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Delhi"],
        size=num_customers
    ),
    
    "signup_date": [
        fake.date_between(start_date="-3y", end_date="today")
        for _ in range(num_customers)
    ],
    
    "customer_rating": np.round(
        np.random.uniform(3.0, 5.0, num_customers), 1
    )
})

print(customers.head())
print("\nShape:", customers.shape)
print("\nMissing values:")
print(customers.isnull().sum())

# Save customers dataset
customers.to_csv("data/raw/customers.csv", index=False)

print("\nCustomers dataset saved successfully!")

##resturant dataset

# Number of restaurants
num_restaurants = 100

restaurants = pd.DataFrame({
    "restaurant_id": [f"R{i:04d}" for i in range(1, num_restaurants + 1)],

    "restaurant_name": [
        fake.company()
        for _ in range(num_restaurants)
    ],

    "restaurant_category": np.random.choice(
        [
            "Indian",
            "Chinese",
            "Italian",
            "Fast Food",
            "South Indian",
            "North Indian",
            "Cafe",
            "Desserts"
        ],
        size=num_restaurants
    ),

    "city": np.random.choice(
        ["Bangalore", "Chennai", "Hyderabad", "Mumbai", "Delhi"],
        size=num_restaurants
    ),

    "restaurant_rating": np.round(
        np.random.uniform(3.0, 5.0, num_restaurants), 1
    ),

    "avg_preparation_time": np.random.randint(
        10, 45, num_restaurants
    )
})

print("\nRestaurant dataset:")
print(restaurants.head())

print("\nShape:", restaurants.shape)

print("\nMissing values:")
print(restaurants.isnull().sum())

restaurants.to_csv(
    "data/raw/restaurants.csv",
    index=False
)

print("Restaurants dataset saved successfully!")

##drivers dataset
# Number of drivers
num_drivers = 500

drivers = pd.DataFrame({
    "driver_id": [f"D{i:04d}" for i in range(1, num_drivers + 1)],

    "driver_age": np.random.randint(
        21, 55, num_drivers
    ),

    "vehicle_type": np.random.choice(
        ["Bike", "Scooter", "Car"],
        size=num_drivers,
        p=[0.45, 0.45, 0.10]
    ),

    "driver_rating": np.round(
        np.random.uniform(3.0, 5.0, num_drivers), 1
    ),

    "experience_years": np.random.randint(
        1, 11, num_drivers
    )
})
print("\nDriver dataset:")
print(drivers.head())

print("\nShape:", drivers.shape)

print("\nMissing values:")
print(drivers.isnull().sum())

drivers.to_csv(
    "data/raw/drivers.csv",
    index=False
)

print("Drivers dataset saved successfully!")

##orders dataset
# Number of orders
num_orders = 10000

orders = pd.DataFrame({
    "order_id": [f"O{i:05d}" for i in range(1, num_orders + 1)],

    "customer_id": np.random.choice(
        customers["customer_id"],
        size=num_orders
    ),

    "restaurant_id": np.random.choice(
        restaurants["restaurant_id"],
        size=num_orders
    ),

    "order_timestamp": pd.to_datetime(
        np.random.choice(
            pd.date_range(
                start="2025-01-01",
                end="2025-03-31",
                freq="h"
            ),
            size=num_orders
        )
    ),

    "order_amount": np.round(
        np.random.uniform(100, 2000, num_orders),
        2
    ),

    "number_of_items": np.random.randint(
        1, 7, num_orders
    ),

    "weather": np.random.choice(
        ["Clear", "Cloudy", "Rainy"],
        size=num_orders,
        p=[0.55, 0.25, 0.20]
    ),

    "traffic_condition": np.random.choice(
        ["Low", "Medium", "High"],
        size=num_orders,
        p=[0.30, 0.45, 0.25]
    ),

    "order_status": np.random.choice(
        ["Completed", "Cancelled"],
        size=num_orders,
        p=[0.92, 0.08]
    )
})
print("\nOrder dataset:")
print(orders.head())

print("\nShape:", orders.shape)

print("\nMissing values:")
print(orders.isnull().sum())

orders.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("Orders dataset saved successfully!")

##deliveries dataset
# Generate delivery data

deliveries = pd.DataFrame({
    "delivery_id": [f"DL{i:05d}" for i in range(1, num_orders + 1)],

    "order_id": orders["order_id"],

    "driver_id": np.random.choice(
        drivers["driver_id"],
        size=num_orders
    ),

    "delivery_distance_km": np.round(
        np.random.uniform(1, 15, num_orders), 2
    ),

    "preparation_time_minutes": np.random.randint(
        10, 45, num_orders
    )
})
deliveries["traffic_condition"] = orders["traffic_condition"].values
deliveries["weather"] = orders["weather"].values
traffic_effect = deliveries["traffic_condition"].map({
    "Low": 0,
    "Medium": 10,
    "High": 20
})
weather_effect = deliveries["weather"].map({
    "Clear": 0,
    "Cloudy": 5,
    "Rainy": 15
})
deliveries["delivery_time_minutes"] = (
    10
    + deliveries["delivery_distance_km"] * 3
    + deliveries["preparation_time_minutes"]
    + traffic_effect
    + weather_effect
    + np.random.normal(0, 5, num_orders)
).round(1)

deliveries["tip_amount"] = np.round(
    orders["order_amount"] * np.random.uniform(
        0.02, 0.15, num_orders
    ),
    2
)
print("\nDelivery dataset:")
print(deliveries.head())

print("\nShape:", deliveries.shape)

print("\nMissing values:")
print(deliveries.isnull().sum())

print("\nAverage delivery time:",
      deliveries["delivery_time_minutes"].mean())

deliveries.to_csv(
    "data/raw/deliveries.csv",
    index=False
)

print("Deliveries dataset saved successfully!")


##reviews dataset
# Number of reviews
num_reviews = 7000

# Select orders that received reviews
review_orders = np.random.choice(
    orders["order_id"],
    size=num_reviews,
    replace=False
)

# Get corresponding customer IDs
review_customers = orders.set_index("order_id").loc[
    review_orders, "customer_id"
].values

# Generate ratings
ratings = np.random.choice(
    [1, 2, 3, 4, 5],
    size=num_reviews,
    p=[0.08, 0.12, 0.20, 0.30, 0.30]
)
def generate_review(rating):

    if rating == 5:
        return np.random.choice([
            "Food was excellent and delivery was very quick.",
            "Amazing food and great delivery experience.",
            "Everything was perfect and arrived on time.",
            "Loved the food, would definitely order again."
        ])

    elif rating == 4:
        return np.random.choice([
            "Good food and the delivery was on time.",
            "Really good experience overall.",
            "Food was tasty and delivery was smooth.",
            "Good service, just a minor delay."
        ])

    elif rating == 3:
        return np.random.choice([
            "Food was okay but delivery took some time.",
            "Average experience, nothing special.",
            "Food was decent but could have been better.",
            "The order was fine overall."
        ])

    elif rating == 2:
        return np.random.choice([
            "Delivery was late and the food was not very good.",
            "Food was cold when it arrived.",
            "The order was delayed and disappointing.",
            "Not happy with the delivery experience."
        ])

    else:
        return np.random.choice([
            "Very late delivery and the food was cold.",
            "Terrible experience, food arrived very late.",
            "Food was disappointing and delivery was extremely slow.",
            "Very poor service, would not order again."
        ])

reviews = pd.DataFrame({
    "review_id": [
        f"RV{i:05d}"
        for i in range(1, num_reviews + 1)
    ],

    "order_id": review_orders,

    "customer_id": review_customers,

    "rating": ratings,

    "review_text": [
        generate_review(rating)
        for rating in ratings
    ]
})
print("\nReview dataset:")
print(reviews.head())

print("\nShape:", reviews.shape)

print("\nMissing values:")
print(reviews.isnull().sum())

print("\nRating distribution:")
print(reviews["rating"].value_counts().sort_index())

reviews.to_csv(
    "data/raw/reviews.csv",
    index=False
)

print("Reviews dataset saved successfully!")

##payments dataset

payments = pd.DataFrame({
    "payment_id": [
        f"P{i:05d}"
        for i in range(1, num_orders + 1)
    ],

    "order_id": orders["order_id"],

    "payment_method": np.random.choice(
        ["UPI", "Credit Card", "Debit Card", "Cash"],
        size=num_orders,
        p=[0.45, 0.25, 0.20, 0.10]
    ),

    "payment_status": np.random.choice(
        ["Completed", "Failed", "Refunded"],
        size=num_orders,
        p=[0.92, 0.05, 0.03]
    ),

    "payment_amount": orders["order_amount"]
})
print("\nPayment dataset:")
print(payments.head())

print("\nShape:", payments.shape)

print("\nMissing values:")
print(payments.isnull().sum())

print("\nPayment status distribution:")
print(payments["payment_status"].value_counts())

payments.to_csv(
    "data/raw/payments.csv",
    index=False
)

print("Payments dataset saved successfully!")