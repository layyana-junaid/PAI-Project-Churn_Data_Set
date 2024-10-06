import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")


age = data['Age'].values
bal = data['Balance'].values

normalized_balance = (data['Balance'].values - np.min(data['Balance'].values)) / (np.max(data['Balance'].values) - np.min(data['Balance'].values))

data['NormalizedBalance'] = normalized_balance
print(data['NormalizedBalance'])

#using correlation to create matrix
matrix = np.corrcoef(data[['CreditScore', 'Age', 'Balance', 'EstimatedSalary']].values.T)

#note this is only applicable for numerical data
print("Correlation Matrix:")
print(matrix)
