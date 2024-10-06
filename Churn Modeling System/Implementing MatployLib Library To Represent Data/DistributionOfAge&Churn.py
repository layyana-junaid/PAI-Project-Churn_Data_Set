import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")

#dividing data in churned and not churned
churned = data[data['Exited'] == 1]
not_churned = data[data['Exited'] == 0]

plt.figure(figsize=(10, 6))

bins = np.linspace(min(data['Age']), max(data['Age']), 20)  # 20 bins

# calculating values for churned and not churned customers
churned_hist, _ = np.histogram(churned['Age'], bins=bins)
not_churned_hist, _ = np.histogram(not_churned['Age'], bins=bins)

# plotting stacked bar chart
plt.bar(bins[:-1], churned_hist, width=np.diff(bins), label='Churned', color='green', edgecolor='black')
plt.bar(bins[:-1], not_churned_hist, width=np.diff(bins), bottom=churned_hist, label='Not Churned', color='yellow', edgecolor='black')

plt.title('Stacked Bar Graph of Age and Churn', fontsize=16)
plt.xlabel('Age', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)

plt.legend()

plt.show()
