import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")

random_sample_indices = np.random.choice(data.index, size=1000, replace=False)
random_sample = data.loc[random_sample_indices]
print(random_sample.head())

# Filtering customers with balance > 100,000 and who churned
high_balance_churners = data[(data['Balance'] > 100000) & (data['Exited'] == 1)]

print(f"Number of high-balance churners: {len(high_balance_churners)}")

# Apply vectorized operations to create a new feature 'HighBalance'
data['HighBalance'] = np.where(data['Balance'] > 100000, 1, 0)
print(data['HighBalance'])
