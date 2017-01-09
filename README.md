# Handbook
Repo of simply explained, important, statistical, numerical and engineering/comp science concepts.

#### Binomial distributions

Binomial distributions are useful to model events that arise in a binomial experiment.  Examples include how many coin flips show heads, how many scratch-off lottery tickets are winners, how many of a doctor's patients die during surgery, and how many free throws I make in one hundred attempts.  Key ingredients of such an experiment include:
A fixed number of repeated, identical, independent trials.  n is usually the parameter chosen to label the number of trials.
Every trial results in either a success, with probability p, or a failure, with probability 1-p.  These must be the only two outcomes for a trial.
The random variable of interest is the total number of trials that ended in a success.

The probability mass function for the binomial distribution is given by:
p(x)=(nx)px(1−p)n−xp(x)=(nx)px(1−p)n−x for x=0,1,2,…,nx=0,1,2,…,n

#### Poisson Distribution
Poisson distributions are useful to model events that seem to take place over and over again in a completely haphazard way.  For example, how many magnitude 8+ earthquakes will take place in a particular year?  Or, how many babies will be born in a large hospital on a particular day?  Or, how many hits will a website get in a particular minute?  Key assumptions for the Poisson model include:
The random variable counts the number of events that take place in a given interval (usually of time or space)
All events take place independently of all other events
The rate at which events take place is constant usually denoted λλ

The probability mass function is given by:
 p(x)=e−λt(λt)xx!p(x)=e−λt(λt)xx! for x=0,1,2,…x=0,1,2,…

#### Normal (Gaussian) Distribution
Normal distributions are used to model far too many different kinds of properties to begin to enumerate in the physical sciences, social sciences, biological sciences, engineering, and on and on.  One reason why it appears so often is the Central limit theorem.  Basically, all properties that arise as an aggregate of many smaller independent (or weakly dependent) contributors will display an approximate normal distribution as long as no small subset of those contributors dominates.

The probability density function for a normal distribution with mean μμ and standard deviation σσ is given by:

#### Gradient Boosted Trees
Gradient Tree Boosting or Gradient Boosted Regression Trees (GBRT) is a generalization of boosting to arbitrary differentiable loss functions.

The first tree we fit on original data. The second tree we fit to residuals to first tree. etc. The residual approximates negative gradient. Final tree is all gradient steps.

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
