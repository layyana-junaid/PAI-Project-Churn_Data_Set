# PAI-Project Proposal
## Data Set: Churn Modelling Dataset
## Group Members: Layyana Junaid(23k-0056), Amna(23k-0066)

### What is Churn Modelling?
#### Churn modelling is a data analysis technique used to predict customer attrition or "churn," which refers to losing clients or customers over time. 
#### This occurs when a customer stops transacting business with a company, such as cancelling his service subscription, not renewing a contract, or changing over to a #### competitor. A churn rate, or sometimes even just the number of customers lost, can quantitatively measure the extent of customer churn.

### 1.Dataset Overview
#### •	Dataset Name: Churn Modelling Dataset
#### •	Source: Kaggle (https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)
#### •	Number of Rows and Columns: The dataset has:
####  o	Rows: 10,000
####  o	Columns: 14
![image](https://github.com/user-attachments/assets/357a1b39-8470-4cc0-bf53-c01aca30e3d7)

### 2. Information Extracted Using Python Libraries
#### Using Python libraries such as pandas, numpy, and sklearn, we will extract and analyze the following information from the dataset:
#### •	Data Cleaning: We will ensure there are no missing or invalid values in the dataset. We'll convert categorical data like Gender and Geography into numeric data for machine learning models.

#### •	Basic Statistics:
####  o	Mean, Median, and Mode: These will give us an idea of the central tendencies of numerical variables like Age, Balance, and EstimatedSalary.
#### o	Standard Deviation and Variance: We will measure the spread of features like CreditScore and Tenure to understand customer behavior variability.
#### •	Correlation Analysis: We'll calculate the correlation between numerical features, such as Age, CreditScore, Balance, and the target variable Exited, to understand how these variables relate to customer churn.
#### •	Predictive Modeling: We will build a machine learning model (e.g., Logistic Regression or Random Forest) to predict customer churn based on these features. The model will help us understand which features (e.g., Age, Geography, Balance, etc.) are the most significant in predicting churn.

### 3. Graph Insights and Data Visualization

#### The purpose of using visualizations like histograms, box plots, and correlation heatmaps is to gain deeper insights into the data and identify patterns and trends. Here are some specific graphs we will create and what insights they will provide:

#### •	Distribution of Age and Churn: A histogram will show how the customer’s age is distributed in the dataset. Overlaying the churn data will help us understand if churn is higher among younger or older customers.
#### Insight: We might observe that churn is higher among younger customers, suggesting the need for targeted retention strategies for that age group.
#### •	Correlation Heatmap: This heatmap will visualize the correlation between different features, highlighting which features (e.g., CreditScore, Balance) are most strongly associated with customer churn.
#### Insight: We may find that customers with a low balance or poor credit score are more likely to churn, suggesting that financial health is a key predictor of churn.
#### •	Boxplots of Balance vs Churn: A boxplot will help us compare the account balance distribution between customers who stayed and those who churned.
#### Insight: If customers with higher balances tend to churn less frequently, the bank may want to focus on increasing customer balances to reduce churn.
#### •	Barplot of Geography and Churn: This plot will help us visualize churn rates across different countries (e.g., France, Germany, Spain).
#### Insight: If we find that churn is higher in a specific region (e.g., Germany), the bank may focus its efforts on improving customer satisfaction and services in that area.

### 4. Enhancing Understanding Through Data Visualization
#### Data visualizations enhance our understanding of the dataset by making complex relationships easier to interpret. For instance, a simple correlation heatmap can help us quickly identify which features are most related to customer churn, guiding our predictive modelling. Histograms and boxplots help us observe the spread and distribution of data, revealing outliers and trends that aren't immediately obvious from statistical summaries alone. By visualizing the data, we can more easily communicate our findings and draw actionable conclusions for improving customer retention strategies.



