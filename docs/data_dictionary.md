# Data Dictionary

## Customers

| Column | Description |
|---|---|
| customer_id | Unique customer identifier |
| age | Customer age |
| gender | Customer gender |
| city | Customer city |
| signup_date | Date when customer joined |
| customer_rating | Customer rating |

## Restaurants

| Column | Description |
|---|---|
| restaurant_id | Unique restaurant identifier |
| restaurant_name | Restaurant name |
| restaurant_category | Cuisine/category |
| city | Restaurant city |
| restaurant_rating | Restaurant rating |
| avg_preparation_time | Average food preparation time in minutes |

## Drivers

| Column | Description |
|---|---|
| driver_id | Unique driver identifier |
| driver_age | Driver age |
| vehicle_type | Type of vehicle used |
| driver_rating | Driver rating |
| experience_years | Driver experience in years |

## Orders

| Column | Description |
|---|---|
| order_id | Unique order identifier |
| customer_id | Customer who placed the order |
| restaurant_id | Restaurant receiving the order |
| order_timestamp | Date and time of order |
| order_amount | Total order amount |
| number_of_items | Number of items ordered |
| weather | Weather condition |
| traffic_condition | Traffic condition |
| order_status | Order completion/cancellation status |

## Deliveries

| Column | Description |
|---|---|
| delivery_id | Unique delivery identifier |
| order_id | Associated order |
| driver_id | Driver assigned to delivery |
| delivery_distance_km | Delivery distance |
| preparation_time_minutes | Food preparation time |
| traffic_condition | Traffic condition during delivery |
| weather | Weather during delivery |
| delivery_time_minutes | Total delivery time |
| tip_amount | Tip given for delivery |

## Reviews

| Column | Description |
|---|---|
| review_id | Unique review identifier |
| order_id | Associated order |
| customer_id | Customer who submitted review |
| rating | Customer rating from 1 to 5 |
| review_text | Written customer feedback |

## Payments

| Column | Description |
|---|---|
| payment_id | Unique payment identifier |
| order_id | Associated order |
| payment_method | Method used for payment |
| payment_status | Payment outcome |
| payment_amount | Amount paid |