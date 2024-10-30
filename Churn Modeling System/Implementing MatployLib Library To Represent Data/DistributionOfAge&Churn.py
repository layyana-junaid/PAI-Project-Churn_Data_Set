import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\k230056\Desktop\23k0056\ab10\Churn_Modelling.csv")
data['Churned'] = data['Exited'].map({0: 'Not Churned', 1: 'Churned'})
plt.figure(figsize=(10, 6))

sns.histplot(data=data, x='Age', hue='Churned', bins=20, multiple='stack', 
             palette=['#DDA0DD', '#9B59B6'], edgecolor='black')
plt.title('Stacked Histogram of Age and Churn', fontsize=18, fontweight='bold', color='#5B2E91')
plt.xlabel('Age', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)

legend_labels = ['Not Churned', 'Churned']
legend_colors = ['#DDA0DD', '#9B59B6']
handles = [plt.Line2D([0], [0], color=color, lw=5) for color in legend_colors]
plt.legend(handles, legend_labels, title='Customer Status', title_fontsize='13', fontsize='12', loc='upper right')

plt.tight_layout()
plt.show()

