import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")

# Check if the Age column has missing values
print(f"Missing values in Age: {data['Age'].isnull().sum()}")
print(f"Missing values in Balance: {data['Balance'].isnull().sum()}")

# Fill missing values in Age column without inplace (correct method)
data['Age'] = data['Age'].fillna(data['Age'].mean())
