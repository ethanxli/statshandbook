# statshandbook
Repo of simply explained, important statistical concepts

#### Gradient Boosted Trees
Gradient Tree Boosting or Gradient Boosted Regression Trees (GBRT) is a generalization of boosting to arbitrary differentiable loss functions.

The first tree we fit on original data. THe second tree we fit to residuals to first tree. etc. The residual approximates negative gradient . final tree is all gradient steps.

#### Hessian (Matrix)
The second order partial derivatives of a function. Used in a second derivative test to find extreme values of functions of more than one variable.


#### Kaplan Meier Estimator
A non-parametric statistic used to estimate the survival function from lifetime data.


#### Newton's method
Newton's method (also known as the Newton–Raphson method), named after Isaac Newton and Joseph Raphson, is a method for finding successively better approximations to the roots (or zeroes) of a real-valued function.


#### Standard deviation
Standard deviation is a measure of dispersion of the data from the mean.

#### Standard error
It is a measure of how precise is our estimate of the mean.
###### Computation of the standard error of the mean
sem<-sd(x)/sqrt(length(x))
###### 95% confidence intervals of the mean
c(mean(x)-2*sem,mean(x)+2*sem)
###### When to use standard deviation? When to use standard error?
It depends. If the message you want to carry is about the spread and variability of the data, then standard deviation is the metric to use. If you are interested in the precision of the means or in comparing and testing differences between means then standard error is your metric. Of course deriving confidence intervals around your data (using standard deviation) or the mean (using standard error) requires your data to be normally distributed. Bootstrapping is an option to derive confidence intervals in cases when you are doubting the normality of your data.
