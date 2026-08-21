# Uber Eats Operational & Customer Intelligence System

## Project Objective

Build an end-to-end machine learning system for Uber Eats to:

- Segment customers and restaurants
- Analyze customer sentiment
- Predict delivery time or tip amount
- Forecast hourly order demand
- Generate data-backed business recommendations

## Project Timeline

- Day 1: Synthetic Data Generation + Git
- Day 2: Customer/Restaurant Segmentation
- Day 3: NLP Sentiment Analysis
- Day 4: Regression
- Day 5: Demand Forecasting
- Day 6: End-to-End ML Pipeline + Business Insights
- Day 7: Finalization + Presentation

## Machine Learning Components

### 1. Customer and Restaurant Segmentation

Customer and restaurant behavior was analyzed using unsupervised learning techniques.

The following techniques were implemented:

* K-Means Clustering
* DBSCAN
* PCA for dimensionality reduction and visualization
* Cluster profiling and interpretation

The segmentation analysis was used to identify customer groups with different ordering behavior and restaurant groups with different operational characteristics.

### 2. NLP Sentiment Analysis

Customer reviews were analyzed to understand overall customer sentiment and identify common complaint themes.

The NLP pipeline included:

* Text cleaning and preprocessing
* Stopword removal
* Lemmatization
* TF-IDF vectorization
* Logistic Regression
* Linear SVM
* VADER sentiment analysis
* Model comparison

The analysis identified delivery-related issues and food quality as major themes in negative customer feedback.

### 3. Delivery Time Prediction

Regression models were used to predict delivery time based on operational and order-related features.

Features included:

* Delivery distance
* Preparation time
* Traffic condition
* Weather condition
* Order amount
* Order hour
* Day of week
* Number of items

The models compared were:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Random Forest Regression

Model performance was evaluated using:

* MAE
* RMSE
* R² Score

Feature importance analysis showed that delivery distance and restaurant preparation time were the strongest drivers of delivery duration.

### 4. Hourly Demand Forecasting

Time-series analysis was performed to forecast hourly Uber Eats order demand.

The forecasting pipeline included:

* Time-series decomposition
* Stationarity testing using the Augmented Dickey-Fuller test
* ARIMA forecasting
* Prophet forecasting
* Model comparison using MAE, RMSE, and MAPE
* Next 24-hour demand forecasting

Prophet achieved slightly better forecasting performance than ARIMA based on the evaluation metrics.

## Key Business Insights

The integrated analysis produced the following insights:

* Customer Cluster 1 represented the highest-value customer segment based on average spending and order frequency.
* Restaurant segments showed differences in revenue, ratings, cancellation rates, and delivery performance.
* Approximately 21% of customer reviews were classified as negative.
* Delivery issues and food quality issues were the most common negative customer experience themes.
* Delivery distance and preparation time were the strongest factors influencing delivery duration.
* Linear Regression achieved the best performance among the evaluated delivery-time prediction models.
* Prophet slightly outperformed ARIMA for hourly demand forecasting.
* Historical and forecasted demand patterns indicated relatively higher demand during specific evening and late-night periods.

## Business Recommendations

Based on the analysis, the following actions are recommended:

1. **Retain high-value customers** through loyalty programs and personalized promotions.

2. **Improve restaurant operations** by identifying restaurant segments with lower ratings or higher cancellation rates.

3. **Reduce delivery delays** by focusing on delivery distance optimization and restaurant preparation time.

4. **Address customer complaints** related to delivery delays and food quality.

5. **Use demand forecasts for capacity planning** by aligning driver availability with predicted high-demand periods.

6. **Monitor operational performance continuously** and update models as new data becomes available.

## Project Structure

```text
uber-eats-ml-capstone/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   └── data_dictionary.md
│
├── models/
│
├── notebooks/
│   ├── day2_customer_segmentation.ipynb
│   ├── day3_nlp_sentiment_analysis.ipynb
│   ├── day4_delivery_time_prediction.ipynb
│   ├── day5_hourly_demand_forecasting.ipynb
│   └── day6_end_to_end_ml_business_insights.ipynb
│
├── outputs/
│   ├── day2_segmentation/
│   ├── day3_nlp/
│   ├── day4_regression/
│   ├── day5_forecasting/
│   └── day6_business_insights/
│
├── src/
│   ├── data_generation.py
│   └── validate_data.py
│
├── README.md
└── requirements.txt
```

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* NLTK
* VADER Sentiment Analysis
* Statsmodels
* Prophet
* Git and GitHub

## Model Limitations

* The project uses synthetic data, so the results may not represent actual Uber Eats customer behavior.
* Clustering results depend on the selected features and clustering parameters.
* Sentiment models may not fully capture sarcasm or complex language.
* Delivery-time predictions do not include all real-world operational factors.
* Demand forecasting accuracy is limited by the amount of historical data available.
* Forecast predictions should be used with uncertainty ranges rather than as exact demand values.

## Future Improvements

Possible improvements include:

* Using real Uber Eats operational data.
* Adding real-time traffic and driver availability data.
* Including geographical and location-based features.
* Using advanced NLP models such as BERT.
* Experimenting with advanced time-series forecasting models.
* Hyperparameter tuning and cross-validation.
* Deploying the models through an automated ML pipeline.
* Building an interactive business dashboard.




