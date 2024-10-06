import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")

X = data[['CreditScore', 'Age', 'Balance', 'EstimatedSalary']].values
y = data['Exited'].values

print(f"Shape of Features (X): {X.shape}")
print(f"Shape of Target (y): {y.shape}")
