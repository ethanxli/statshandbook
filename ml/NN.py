import numpy as np


class NN():

    def __init__(self):
        self.inputLayerSize = 2
        self.hiddenLayerSize = 3
        self.outputLayerSize = 1


        #weights initialized as ranodm.

        #weight from input to hidden
        self.W1 = np.random.rand(self.inputLayerSize, self.hiddenLayerSize)

        #weight from hidden to output
        self.W1 = np.random.rand(self.hiddenLayerSize, self.outputLayerSize)


    def fwdProp(self, X):
        '''
        propogate inputs through network:
        X = inputs  (examples * inputLayerSize)
        z2 = XW_1   (3x2)*(2x3)
        a2 = f(z2)  (3x3)
        z3 = aW_2   (3x3)*(3x1)
        y = f(z3)   (3x1)
        '''


        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2,self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat


    def sigmoid(self, z):
        #example activation function- the sigmoid
        return 1/(1+np.exp(-z))


    def sigmoidPrime(self,z):
        return np.exp(-z)/((1+np.exp(-z))**2)


    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5*sum((y-self.yHat)**2)
        return J

    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)

        return dJdW1, dJdW2
