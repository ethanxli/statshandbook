# Handbook
Repo of simply explained, important, statistical, numerical and engineering/comp science concepts.

### Bootstrapping

TODO


### Bayesian Inference
Bayesian inference is a method of statistical inference in which Bayes' theorem is used to update the probability for a hypothesis as more evidence or information becomes available.

##### Steps

1. Formulate a probability model for the data.
2. Decide on a prior distribution, which quantifies the uncertainty in the values of
the unknown model parameters before the data are observed.
 3. Observe the data, and construct the likelihood function (see Section 2.3) based on
the data and the probability model formulated in step 1. The likelihood is then
combined with the prior distribution from step 2 to determine the posterior distribution,
which quantifi es the uncertainty in the values of the unknown model
parameters after the data are observed.
 4. Summarize important features of the posterior distribution, or calculate quantities
of interest based on the posterior distribution. These quantities constitute statistical
outputs, such as point estimates and intervals.

### Binomial distributions

Binomial distributions are useful to model events that arise in a binomial experiment.  Examples include how many coin flips show heads, how many scratch-off lottery tickets are winners, how many of a doctor's patients die during surgery, and how many free throws I make in one hundred attempts.  Key ingredients of such an experiment include:
A fixed number of repeated, identical, independent trials.  n is usually the parameter chosen to label the number of trials.
Every trial results in either a success, with probability p, or a failure, with probability 1-p.  These must be the only two outcomes for a trial.
The random variable of interest is the total number of trials that ended in a success.

The probability mass function for the binomial distribution is given by:
p(x)=(nx)px(1−p)n−xp(x)=(nx)px(1−p)n−x for x=0,1,2,…,nx=0,1,2,…,n

### Eigenvalues and Eigenvectors

A short explanation

Consider a matrix AA, for an example one representing a physical transformation. When this matrix is used to transform a given vector x the result is y=Ax.

Now an interesting question is:

Are there any vectors x which does not change it's direction under this transformation, but allow the vector magnitude to vary by scalar λ?
Such a question is of the form
Ax=λx
So, such special x are called eigenvector(s) and the change in magnitude depends on the eigenvalue λλ.

We say that a number is the eigenvalue for this square matrix if and only if there exists a nonzero vector x such that Ax = λx where:

A is the square matrix
x is the nonzero vector
λ is a nonzero value.

In this circumstance, λ is the eigenvalue and x is the eigenvector.

Mathematically, the natural frequency can be characterized by the eigenvalue of the smallest magnitude.

Eigenvectors are the "axes" (directions) along which a linear transformation acts simply by "stretching/compressing" and/or "flipping"; eigenvalues give you the factors by which this compression occurs.


### (Gaussian) Distribution
Normal distributions are used to model far too many different kinds of properties to begin to enumerate in the physical sciences, social sciences, biological sciences, engineering, and on and on.  One reason why it appears so often is the Central limit theorem.  Basically, all properties that arise as an aggregate of many smaller independent (or weakly dependent) contributors will display an approximate normal distribution as long as no small subset of those contributors dominates.

The probability density function for a normal distribution with mean μ and standard deviation σ is given by:

1/sqrt(2pi) * e ^ (-x^2/2)

### Gradient Boosted Trees
Gradient Tree Boosting or Gradient Boosted Regression Trees (GBRT) is a generalization of boosting to arbitrary differentiable loss functions.

The first tree we fit on original data. The second tree we fit to residuals to first tree. etc. The residual approximates negative gradient. Final tree is all gradient steps.

### Hessian (Matrix)
The second order partial derivatives of a function. Used in a second derivative test to find extreme values of functions of more than one variable.

### Kaplan Meier Estimator
A non-parametric statistic used to estimate the survival function from lifetime data.

### Lagrange Multiplier

In mathematical optimization, the method of Lagrange multipliers is a strategy for finding the local maxima and minima of a function subject to equality constraints.

We can do this by first find extreme points of f, which are points where the gradient det(f) is zero, or, each of the partial derivatives is zero. If we’re lucky, points like this that we find will turn out to be (local) maxima, but they can also be minima or saddle points. We can tell the different cases apart by a variety of means, including checking properties of the second derivatives or simple inspecting the
function values


For instance (see Figure 1), consider the optimization problem

maximize f(x, y)
subject to g(x, y) = c.


### Newton's method
Newton's method (also known as the Newton–Raphson method), named after Isaac Newton and Joseph Raphson, is a method for finding successively better approximations to the roots (or zeroes) of a real-valued function.

### Poisson Distribution
Poisson distributions are useful to model events that seem to take place over and over again in a completely haphazard way.  For example, how many magnitude 8+ earthquakes will take place in a particular year?  Or, how many babies will be born in a large hospital on a particular day?  Or, how many hits will a website get in a particular minute?  Key assumptions for the Poisson model include:
The random variable counts the number of events that take place in a given interval (usually of time or space)
All events take place independently of all other events
The rate at which events take place is constant usually denoted λλ

The probability mass function is given by:
 p(x)=e−λt(λt)xx!p(x)=e−λt(λt)xx! for x=0,1,2,…x=0,1,2,…



### Probability Density Function
The integral of a probability density function gives the probability that a random variable falls within some interval.
Probability mass functions are used for discrete distributions. It assigns a probability to each point in the sample space.


### Standard deviation
Standard deviation is a measure of dispersion of the data from the mean.
STDEV = sqrt( 1/n * sum (xi - u)^2 )

### Standard error
It is a measure of how precise is our estimate of the mean.
##### Computation of the standard error of the mean
sem<-sd(x)/sqrt(length(x))
##### 95% confidence intervals of the mean
c(mean(x)-2*sem,mean(x)+2*sem)
##### When to use standard deviation? When to use standard error?
It depends. If the message you want to carry is about the spread and variability of the data, then standard deviation is the metric to use. If you are interested in the precision of the means or in comparing and testing differences between means then standard error is your metric. Of course deriving confidence intervals around your data (using standard deviation) or the mean (using standard error) requires your data to be normally distributed. Bootstrapping is an option to derive confidence intervals in cases when you are doubting the normality of your data.


### Student's T-Distribution
The t-distribution is symmetric and bell-shaped, like the normal distribution, but has heavier tails, meaning that it is more prone to producing values that fall far from its mean. This makes it useful for understanding the statistical behavior of certain types of ratios of random quantities
