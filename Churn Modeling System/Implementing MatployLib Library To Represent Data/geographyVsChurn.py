import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")
churn_by_geo = data.groupby(['Geography', 'Exited']).size().unstack()

plt.figure(figsize=(12, 6))

churn_by_geo.plot(kind='bar', stacked=True, color=['lightgreen', 'yellow'], edgecolor='black')

plt.title('Barplot of Geography and Churn', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.legend(['Not Churned', 'Churned'], title='Churn Status')

plt.xticks(rotation=0)

plt.show()



