'''Graphical Representation of Churn Modelling Data Set'''
'''Group Members: Layyana Junaid(23k-0056), Amna (23k-0066)'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"Churn_Modelling.csv")

'''Statistical Calculations'''
def print_statistical_calculations():
    # calculating mean and median of the following data sets Age,
    # Balance and EstimatedSalary Columns
    '''first we will convert data(that we want to work upon) into numpy arrays'''
    age = data["Age"].values
    balance = data["Balance"].values
    estimated_salary = data["EstimatedSalary"].values

    '''calculating the mean'''
    age_mean = np.mean(age)
    balance_mean = np.mean(balance)
    estimated_salary_mean = np.mean(estimated_salary)

    '''calculating the median'''
    age_median = np.median(age)
    balance_median = np.median(balance)
    estimated_salary_median = np.median(estimated_salary)
    print(f"Mean of Age: {age_mean}")
    print(f"Median of Age: {age_median}")
    print(f"Mean of Balance: {balance_mean}")
    print(f"Median of Balance: {balance_median}")
    print(f"Mean of Estimated Salary: {estimated_salary_mean}")
    print(f"Median of Estimated Salary: {estimated_salary_median}")

'''Performing Data Cleaning'''
def data_cleaning():
    print(f"Missing values in Age: {data['Age'].isnull().sum()}")
    print(f"Missing values in Balance: {data['Balance'].isnull().sum()}")
    print(f"Missing values in Estimated Salary: {data['EstimatedSalary'].isnull().sum()}")
    print(f"Missing values in Credit Score: {data['CreditScore'].isnull().sum()}")

    '''Filling in the place of missing values'''
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    data['Balance'] = data['Balance'].fillna(data['Balance'].mean())
    data['EstimatedSalary'] = data['EstimatedSalary'].fillna(data['EstimatedSalary'].mean())
    data['CreditScore'] = data['CreditScore'].fillna(data['CreditScore'].mean())


'''Graphical Representation of the following data set'''
#histogram to show the distribution of age
plt.title("Distribution of Age")
plt.xlabel("Age")
sns.histplot(data=data,x="Age",color="purple",kde=True)
plt.show()

#box plot to show the distribution of the boxplot
plt.title("Distribution of Balance")
plt.ylabel("Balance")
sns.boxplot(data=data, y="Balance", color="purple", width=0.25)
plt.show()

#countplot to represent distribution of geography
plt.xlabel("Geography")
plt.title("Distribution of Geography")
sns.countplot(data=data, x='Geography', color="purple", width=0.3)
plt.show()

#scatter plot to show the relation of age and balance
purple_palette = {0: '#b19cd9', 1: '#800080'}
plt.xlabel("Age")
plt.ylabel("Balance")
plt.title("Age vs Balance")
sns.scatterplot(data=data, x='Age', y='Balance',  hue='Exited', palette=purple_palette)
plt.show()

#heating map
'''information to make correlation heatmap'''
features = data[['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Exited']]
correlation_matrix = features.corr()
plt.figure(figsize=(10, 8))

# creating the heatmap
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='Purples', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap', fontsize=16)
plt.show()