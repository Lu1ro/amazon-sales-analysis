\# 📊 Amazon Product Sales Analysis



!\[Python](https://img.shields.io/badge/Python-3.10%2B-blue)

!\[Libraries](https://img.shields.io/badge/Library-Pandas%20%7C%20Seaborn-green)

!\[Status](https://img.shields.io/badge/Status-Completed-success)



\## 📌 Executive Summary

This project analyzes a dataset of over 1,400 Amazon products to understand \*\*pricing strategies\*\*, \*\*discount effectiveness\*\*, and \*\*customer sentiment\*\*. 



\*\*Key Business Question:\*\* \*Do higher discounts actually lead to better customer ratings or higher sales volume?\*



\## 🔍 Key Findings \& Insights

Based on the data analysis, the following trends were identified:



1\.  \*\*Deep Discount Strategy:\*\* The average discount across products is \*\*47.6%\*\*. A significant portion of inventory uses a "High Markup, High Discount" pricing model.

2\.  \*\*Rating Inflation:\*\* The average product rating is \*\*4.1/5.0\*\*, which is unusually high. This suggests a survivorship bias (only good products stay listed).

3\.  \*\*Price-Rating Independence:\*\* There is \*\*no strong correlation\*\* between the price of a product and its rating. Expensive items do not guarantee higher customer satisfaction.



\## 📈 Visualizations



\### 1. Market Composition

\*Electronics dominate the dataset, followed closely by Home \& Kitchen.\*

!\[Top Categories](images/1\_top\_categories.png)



\### 2. Pricing Strategy

\*The majority of products are discounted between 30% and 60%.\*

!\[Discount Distribution](images/2\_discount\_distribution.png)



\### 3. Price vs. Quality Perception

\*Scatter plot analysis shows that customer satisfaction (rating) remains stable regardless of price point.\*

!\[Price vs Rating](images/3\_price\_vs\_rating.png)



\## 🛠️ Methodology

\* \*\*Data Cleaning:\*\* Handled currency symbols (`₹`) and missing values.

\* \*\*Feature Engineering:\*\* Extracted categories and converted numeric types.

\* \*\*Analysis:\*\* Univariate and Bivariate analysis using Pandas \& Seaborn.



\## 🚀 How to Run

1\. Clone the repository.

2\. Install dependencies:

&nbsp;  ```bash

&nbsp;  pip install -r requirements.txt

