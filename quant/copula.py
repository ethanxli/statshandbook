#!/usr/bin/env python

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

np.random.seed()
N = 1000
a1 = np.random.uniform(0, 1.0 ,N)
a2 = np.random.uniform(0, 1.0 ,N)

mu = np.array([0,0])
sigma = np.array([[1.0,0.2],[0.2,1.0]])

#inverse CDF
b1 = norm.ppf(a1)
b2 = norm.ppf(a2)
b = np.c_[b1,b2]

#Linear Transformation
mu_array = np.tile(mu,N).reshape(N,2)
Q = np.linalg.cholesky(sigma)
#np.dot(Q,Q.T) #check
c = np.dot(b,Q) + mu_array

#CDF
d1 = norm.cdf(c[:,0])
d2 = norm.cdf(c[:,1])

rand1 = norm.ppf(d1)
rand2 = norm.ppf(d2)
rand = np.c_[rand1,rand2]

#Plot
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
plotx = np.linspace(-10,10,100)
rand1_CDF = norm.cdf(x=plotx, loc=np.mean(rand1), scale=np.std(rand1))
ax1.scatter(plotx,rand1_CDF)
ax2 = fig.add_subplot(2,2,2)
ax2.hist(rand1)
ax3 = fig.add_subplot(2,2,3)
rand2_CDF = norm.cdf(x=plotx, loc=np.mean(rand2), scale=np.std(rand2))
ax3.scatter(plotx,rand2_CDF)
ax4 = fig.add_subplot(2,2,4)
ax4.hist(rand2)
fig.tight_layout()
plt.show()

fig2 = plt.figure()
ax2_1 = fig2.add_subplot(1,1,1)
ax2_1.scatter(rand1,rand2)
fig2.show()

#########test#########

#Caluculate
S = np.corrcoef(rand[:,0],rand[:,1])
C = np.diag([np.std(rand[:,0]),np.std(rand[:,1])])
sample_sigma2 = np.dot(np.dot(S,C),C)
print(sample_sigma2)
