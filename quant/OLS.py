import numpy as np
from sklearn import datasets, linear_model


#The OLS method minimizes the sum of squared residuals, and leads to a closed-form expression
# for the estimated value of the unknown parameter B:
# B = (X^TX)^-1 X^T y

#with intercept, add '1' column to X
y = np.array([1,2,3,4,5])
X = np.matrix([[1,4],
               [2,3],
               [3.3,4.3],
               [14.5,4.2],
               [4,6.3]])

c1 = np.linalg.inv(np.matmul(X.T,X))
beta = np.matmul(np.matmul(c1,X.T), y)

print beta


#compare to sklearn LinearRegression

# Create linear regression object
regr = linear_model.LinearRegression(fit_intercept=False)

# Train the model using the training sets
regr.fit(X, y)

# The coefficients
print('Coefficients: \n', regr.coef_)
