'''Graphical Representation of Churn Modelling Data Set'''
'''Group Members: Layyana Junaid(23k-0056), Amna (23k-0066)'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
from tkinter import Tk, Button, Label

#Load data
data = pd.read_csv(r"Churn_Modelling.csv")

#Data cleaning and preprocessing
def data_cleaning():
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    data['Balance'] = data['Balance'].fillna(data['Balance'].mean())
    data['EstimatedSalary'] = data['EstimatedSalary'].fillna(data['EstimatedSalary'].mean())
    data['CreditScore'] = data['CreditScore'].fillna(data['CreditScore'].mean())

data_cleaning()

#Preprocessing for ML
data = data.drop(columns=['RowNumber', 'CustomerId', 'Surname'])
labelEncoder = LabelEncoder()
data['Geography'] = labelEncoder.fit_transform(data['Geography'])
data['Gender'] = labelEncoder.fit_transform(data['Gender'])

X = data.drop('Exited', axis=1)
y = data['Exited']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.fit_transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

#Tkinter GUI setup
root = Tk()
root.title("Customer Churn Data Analysis")

heading_label = Label(
    root,
    text="Customer Churn Data Analysis Dashboard",
    font=("Arial", 16, "bold"),
    fg="white",
    bg="purple",
    padx=10,
    pady=10
)
heading_label.pack(fill="x") 

def show_age_distribution():
    plt.title("Distribution of Age")
    plt.xlabel("Age")
    sns.histplot(data=data, x="Age", color="Purple", kde=True)
    plt.show()

def show_balance_distribution():
    plt.title("Distribution of Balance")
    plt.ylabel("Balance")
    sns.boxplot(data=data, y="Balance", color="thistle", width=0.25)
    plt.show()

def show_pair_plot():
    sns.pairplot(data, vars=['CreditScore', 'Age', 'Balance', 'EstimatedSalary'], hue='Exited', diag_kind='kde', palette='Purples')
    plt.suptitle('Pair Plot of Key Features with Churn Status', y=1.02)
    plt.show()

def show_age_vs_balance_scatter():
    plt.xlabel("Age")
    plt.ylabel("Balance")
    plt.title("Age vs Balance")
    purple_palette = {0: '#b19cd9', 1: '#800080'}
    sns.scatterplot(data=data, x='Age', y='Balance', hue='Exited', palette=purple_palette)
    plt.show()

def show_correlation_heatmap():
    numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
    correlational_matrix = data[numerical_cols + ['Exited']].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlational_matrix, annot=True, cmap='Purples')
    plt.title('Correlation Heatmap')
    plt.show()

def show_range_barplot():
    numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
    range_stats = data[numerical_cols].apply(lambda x: x.max() - x.min())
    plt.figure(figsize=(12, 6))
    sns.barplot(x=range_stats.index, y=range_stats.values, palette='Purples')
    plt.title('Range of Numerical Features')
    plt.xlabel('Numerical Feature')
    plt.ylabel('Range (Max - Min)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

def show_knn_confusion_matrix():
    cm = confusion_matrix(y_test, y_pred_knn)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', xticklabels=["Stayed", "Churned"], yticklabels=["Stayed", "Churned"])
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()

def show_roc_curve():
    fpr, tpr, _ = roc_curve(y_test, knn.predict_proba(X_test_scaled)[:, 1])
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(6, 5))
    plt.plot(fpr, tpr, color='thistle', lw=2, label=f'KNN (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='lightpink', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()

def show_violin_balance():
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x='Exited', y='Balance', palette='Purples')
    plt.title('Balance Distribution by Churn Status')
    plt.show()

def show_violin_credit_score():
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=data, x='Exited', y='CreditScore', palette='Purples')
    plt.title('Credit Score Distribution by Churn Status')
    plt.show()


Button(root, text="Age Distribution", command=show_age_distribution, width=30).pack(pady=5)
Button(root, text="Balance Distribution", command=show_balance_distribution, width=30).pack(pady=5)
Button(root, text="Pair Plot of Features", command=show_pair_plot, width=30).pack(pady=5)
Button(root, text="Age vs Balance Scatter", command=show_age_vs_balance_scatter, width=30).pack(pady=5)
Button(root, text="Correlation Heatmap", command=show_correlation_heatmap, width=30).pack(pady=5)
Button(root, text="Range Barplot", command=show_range_barplot, width=30).pack(pady=5)
Button(root, text="KNN Confusion Matrix", command=show_knn_confusion_matrix, width=30).pack(pady=5)
Button(root, text="ROC Curve", command=show_roc_curve, width=30).pack(pady=5)
Button(root, text="Violin Plot (Balance)", command=show_violin_balance, width=30).pack(pady=5)
Button(root, text="Violin Plot (Credit Score)", command=show_violin_credit_score, width=30).pack(pady=5)

root.mainloop()
