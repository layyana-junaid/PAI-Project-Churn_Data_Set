mport pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\PAIPROJECT\Churn_Modelling.csv")

#converting columns to numpy arrays to analyse them
age = data['Age'].values
bal = data['Balance'].values

#now we will implement mean, median, standard deviation and variance on these arrays
mean = np.mean(age)
median = np.median(age)
sd = np.std(age)
variation = np.var(age)

mean_ = np.mean(bal)
median_ = np.median(bal)
sd_ = np.std(bal)
variation_ = np.var(bal)

print("Analysis for Age: ")
print("Mean: ", mean, ", Median: ", median, ", Standard Deviation: ", sd, ", Variation: ", variation, "\n")
print("Analysis for Balance: ")
print("Mean: ", mean_, ", Median: ", median_, ", Standard Deviation: ", sd_, ", Variation: ", variation_)

#plotting histogram to represnt the anaysis of age and balance
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.hist(age, bins=20, color='blue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(bal, bins=20, color='green', edgecolor='black')
plt.title('Balance Distribution')
plt.xlabel('Balance')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

#plotting box plot to represent  the analysis between age and balance
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(age, vert=False, patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Age Box Plot')

plt.subplot(1, 2, 2)
plt.boxplot(bal, vert=False, patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Balance Box Plot')

plt.tight_layout()
plt.show()

#plotting bar graphs
categories = ['Age', 'Balance']
mean_values = [mean, mean_]

plt.figure(figsize=(8, 5))
plt.bar(categories, mean_values, color=['blue', 'green'])
plt.title('Mean of Age and Balance')
plt.ylabel('Mean Value')
plt.xlabel('Categories')
plt.show()
