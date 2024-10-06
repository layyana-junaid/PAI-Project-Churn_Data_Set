### 1. Features and Labels (Independent and Dependent Variables)
In machine learning, we typically divide the dataset into:
Features (X): The independent variables used to make predictions.
Labels (y): The dependent variable, also known as the target, which we want to predict.
##### Explanation of the Code:

###### Features and labels (independent and dependent variables)
X = df[['CreditScore', 'Age', 'Balance', 'EstimatedSalary']].values  # Features (NumPy array)
y = df['Exited'].values  # Target variable (NumPy array)
X = df[['CreditScore', 'Age', 'Balance', 'EstimatedSalary']].values:

This line extracts specific columns from the DataFrame df to create the feature matrix X.
The features selected here are ['CreditScore', 'Age', 'Balance', 'EstimatedSalary'], which are the independent variables (factors that may influence whether a customer leaves or stays).
The .values part converts the selected columns into a NumPy array. In machine learning, we often work with NumPy arrays because they are more efficient and compatible with most machine learning libraries (like scikit-learn).
Features selected:

CreditScore: A customer’s credit score.
Age: The age of the customer.
Balance: The balance in the customer’s bank account.
EstimatedSalary: The estimated salary of the customer.
y = df['Exited'].values:

This line extracts the target variable Exited from the DataFrame df. 
The Exited column represents whether the customer has churned (left the bank) or not (churn modeling).
y represents the dependent variable or target because it's what we are trying to predict (0 means the customer stayed, and 1 means they exited the bank).

### 2. Shape of Features (X) and Target (y)

print(f"Shape of Features (X): {X.shape}")
print(f"Shape of Target (y): {y.shape}")

This code prints out the shape of the X and y arrays. 
##### The shape tells you how many rows (samples) and columns (features) are in your data.

X.shape: This will print the shape of the feature matrix X. It will give you two values:

The number of rows (samples/customers).
The number of columns (features). In this case, we have 4 features: CreditScore, Age, Balance, and EstimatedSalary.
y.shape: This prints the shape of the target variable array y, which contains only one column (whether the customer churned or not). 
The shape will show the number of rows (which should be the same as X) but only one column since it's a single target variable.


###### Why This Step is Important:
##### Features (X): These are the inputs the machine learning algorithm will use to predict customer churn.
##### Target (y): This is what the algorithm is trying to learn (whether a customer exits or stays), based on the features.

##### Together, this step sets up the data for training a machine learning model, such as logistic regression or decision trees, which will learn to predict customer churn based on the provided features.







