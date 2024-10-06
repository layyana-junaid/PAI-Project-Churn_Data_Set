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
