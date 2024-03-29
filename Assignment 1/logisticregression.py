# -*- coding: utf-8 -*-
"""LogisticRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GEh79Sj_T-uq6E8XvHCFykxaSwLycfFU
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.special import expit


class Logistic_Regression_batch:
    def __init__(self, lr, iter):
        self.lr = lr
        self.iter = iter
        self.weight = None
        self.history = None
        return

    def sigmoid(self, X):
        a = expit(np.dot(X, self.weight))
        return a

    def classify(self, prob):
        if prob >= 0.5:
            return 1
        else:
            return 0

    def gradient(self, X, Y):
        grad_E = np.zeros(X.shape[1])
        cnt = 0
        for n in range(X.shape[0]):
            t_n = Y[n]
            X_n = X.iloc[n, :]
            y_n = self.sigmoid(X_n)
            # Gradient of Error function
            grad_E += (y_n-t_n)*X_n
            cnt += 1
        return grad_E/cnt

    def cost(self, X, Y):
        cst = 0.
        for n in range(X.shape[0]):
            t_n = Y[n]
            X_n = X.iloc[n, :]
            y_n = self.sigmoid(X_n)
            if t_n == 1:
                t_n -= 0.000001
            if y_n == 1:
                y_n -= 0.000001
            # Gradient of Error function
            cst += t_n*np.log(y_n)+(1-t_n)*np.log(1-y_n)
            print("Cost: "+str(cst))
        cst *= -1.
        return cst

    def fit(self, X, Y):
        # Add a bias column of all 1s
        X["bias"] = 1
        # Initialize the weights to 0
        self.weight = np.ones(X.shape[1])
        self.history = []
        # Run the gradient descent algorithm
        for i in range(self.iter):
            # Update the weight based on the gradient with the current weight vector
            self.weight -= self.lr*self.gradient(X, Y)
            # Count misclassifications
            misclassifications = 0
            # Print the misclassifications
            if i % 10 == 0 or i < 10:
                for j in range(X.shape[0]):
                    X_j = X.iloc[j, :]
                    Y_j = Y.iloc[j]
                    if self.classify(self.sigmoid(X_j)) != Y_j:
                        misclassifications += 1
                self.history.append((i, self.cost(X, Y)))
                print(self.weight)
                print("misclassifications:")
                print(misclassifications)
                print("epochs:")
                print(i)
        return

    def predict(self, X):
        X["bias"] = 1
        prediction = []
        for i in range(X.shape[0]):
            X_i = X.iloc[i, :]
            prediction.append(self.classify(self.sigmoid(X_i)))
        return prediction


class Logistic_Regression_stochastic:
    def __init__(self, lr, iter):
        self.lr = lr
        self.iter = iter
        self.weight = None
        self.history = None
        return

    def sigmoid(self, X):
        a = expit(np.dot(X, self.weight))
        return a

    def classify(self, prob):
        if prob >= 0.5:
            return 1
        else:
            return 0

    def fit(self, X, Y):
        # Add a bias column of all 1s
        X["bias"] = 1
        # Initialize the weights to 0
        self.weight = np.ones(X.shape[1])
        self.history = []
        # Run the gradient descent algorithm
        for i in range(self.iter):
            # Update the weight based on the gradient with the current weight vector
            for n in range(X.shape[0]):
                grad_E = np.zeros(X.shape[1])
                t_n = Y[n]
                X_n = X.iloc[n, :]
                y_n = self.sigmoid(X_n)
                # Gradient of Error function
                grad_E += (y_n-t_n)*X_n
                self.weight -= self.lr*grad_E
            # Count misclassifications
            misclassifications = 0
            # Print the misclassifications
            if i % 10 == 0 or i < 10:
                for j in range(X.shape[0]):
                    X_j = X.iloc[j, :]
                    Y_j = Y.iloc[j]
                    if self.classify(self.sigmoid(X_j)) != Y_j:
                        misclassifications += 1
                self.history.append((i, self.cost(X, Y)))
                print(self.weight)
                print("misclassifications:")
                print(misclassifications)
                print("epochs:")
                print(i)
        return

    def predict(self, X):
        X["bias"] = 1
        prediction = []
        for i in range(X.shape[0]):
            X_i = X.iloc[i, :]
            prediction.append(self.classify(self.sigmoid(X_i)))
        return prediction

    def cost(self, X, Y):
        cst = 0.
        for n in range(X.shape[0]):
            t_n = Y[n]
            X_n = X.iloc[n, :]
            y_n = self.sigmoid(X_n)
            if t_n == 1:
                t_n -= 0.000001
            if y_n == 1:
                y_n -= 0.000001
            # Gradient of Error function
            cst += t_n*np.log(y_n)+(1-t_n)*np.log(1-y_n)
            print("Cost: "+str(cst))
        cst *= -1.
        return cst


class Logistic_Regression_mini_batch:
    def __init__(self, lr, iter):
        self.lr = lr
        self.iter = iter
        self.weight = None
        self.history = None
        return

    def sigmoid(self, X):
        a = expit(np.dot(X, self.weight))
        return a

    def classify(self, prob):
        if prob >= 0.5:
            return 1
        else:
            return 0

    def fit(self, X, Y):
        # Add a bias column of all 1s
        X["bias"] = 1
        # Initialize the weights to 0
        self.weight = np.ones(X.shape[1])
        self.history = []
        # Run the gradient descent algorithm
        for i in range(self.iter):
            # Update the weight based on the gradient with the current weight vector
            grad_E = np.zeros(X.shape[1])
            for n in range(X.shape[0]):
                t_n = Y[n]
                X_n = X.iloc[n, :]
                y_n = self.sigmoid(X_n)
                # Gradient of Error function
                grad_E += (y_n-t_n)*X_n
                if n % 20 == 0:  # Batch strength is 20
                    self.weight -= self.lr*grad_E
                    grad_E = grad_E = np.zeros(X.shape[1])
                elif n == X.shape[0]-1:
                    self.weight -= self.lr*grad_E
            # Count misclassifications
            misclassifications = 0
            # Print the misclassifications
            if i % 10 == 0 or i < 10:
                for j in range(X.shape[0]):
                    X_j = X.iloc[j, :]
                    Y_j = Y.iloc[j]
                    if self.classify(self.sigmoid(X_j)) != Y_j:
                        misclassifications += 1
                self.history.append((i, self.cost(X, Y)))
                print(self.weight)
                print("misclassifications:")
                print(misclassifications)
                print("epochs:")
                print(i)
        return

    def predict(self, X):
        X["bias"] = 1
        prediction = []
        for i in range(X.shape[0]):
            X_i = X.iloc[i, :]
            prediction.append(self.classify(self.sigmoid(X_i)))
        return prediction

    def cost(self, X, Y):
        cst = 0.
        for n in range(X.shape[0]):
            t_n = Y[n]
            X_n = X.iloc[n, :]
            y_n = self.sigmoid(X_n)
            if t_n == 1:
                t_n -= 0.000001
            if y_n == 1:
                y_n -= 0.000001
            # Gradient of Error function
            cst += t_n*np.log(y_n)+(1-t_n)*np.log(1-y_n)
            print("Cost: "+str(cst))
        cst *= -1.
        return cst


df = pd.read_csv("feature_engineering_2.csv")
# df = pd.read_csv("data.csv")
df = df.dropna()

arguments = sys.argv

if (arguments[4] == "rm-corr"):
    # Create correlation matrix
    corr_matrix = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))

    # Find features with correlation greater than 0.95
    to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

    # Drop features
    df.drop(to_drop, axis=1, inplace=True)

if (arguments[5] == "rm-outliers"):
    pass

tr = df.iloc[:375, :]
test = df.iloc[375:, :]
y = tr.iloc[:, 1]
y_test = test.iloc[:, 1]

tr = tr.drop(tr.columns[[0, 1]], axis=1)
test = test.drop(test.columns[[0, 1]], axis=1)
y.replace('M', 1, inplace=True)
y.replace('B', 0, inplace=True)
y

test

tr


lr = float(arguments[1])
epochs = int(arguments[2])
type = arguments[3]

y_test.replace('M', 1, inplace=True)
y_test.replace('B', 0, inplace=True)

print("TESTING COMMAND LINE ARGS")
print(lr)
print(epochs)
print(type)
if type == "batch":
    model = Logistic_Regression_batch(lr, epochs)
    model.fit(tr, y)
    predicted = model.predict(test)

    count = 0
    for i in range(len(predicted)):
        print(str(predicted[i])+'-'+str(y_test.iloc[i]))
        if predicted[i] != y_test.iloc[i]:
            count += 1

    print("PREDICTED DATA")
    print(predicted)
    print("TEST DATA")
    print(y_test)
    print("NO OF MISCLASSIFICATIONS ON TEST DATA")
    print(count)

    print("PLOTTING DATA")
    points = model.history

    # extract x and y values from each tuple
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    # plot the points
    plt.plot(x, y, 'ro')

    # add axis labels and a title
    plt.xlabel('epochs')
    plt.ylabel('cost')
    plt.title(type)

    # display the plot
    plt.show()
elif type == "mini-batch":
    model = Logistic_Regression_mini_batch(lr, epochs)
    model.fit(tr, y)
    predicted = model.predict(test)

    count = 0
    for i in range(len(predicted)):
        print(str(predicted[i])+'-'+str(y_test.iloc[i]))
        if predicted[i] != y_test.iloc[i]:
            count += 1

    print("PREDICTED DATA")
    print(predicted)
    print("TEST DATA")
    print(y_test)
    print("NO OF MISCLASSIFICATIONS ON TEST DATA")
    print(count)

    print("PLOTTING DATA")
    points = model.history

    # extract x and y values from each tuple
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    # plot the points
    plt.plot(x, y, 'ro')

    # add axis labels and a title
    plt.xlabel('epochs')
    plt.ylabel('cost')
    plt.title(type)

    # display the plot
    plt.show()
elif type == "stochastic":
    model = Logistic_Regression_stochastic(lr, epochs)
    model.fit(tr, y)
    predicted = model.predict(test)

    count = 0
    for i in range(len(predicted)):
        print(str(predicted[i])+'-'+str(y_test.iloc[i]))
        if predicted[i] != y_test.iloc[i]:
            count += 1

    print("PREDICTED DATA")
    print(predicted)
    print("TEST DATA")
    print(y_test)
    print("NO OF MISCLASSIFICATIONS ON TEST DATA")
    print(count)
    print("MODEL:")
    print(type)
    print("COSTS:")
    print(model.history)

    print("PLOTTING DATA")
    points = model.history

    # extract x and y values from each tuple
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    # plot the points
    plt.plot(x, y, 'ro')

    # add axis labels and a title
    plt.xlabel('epochs')
    plt.ylabel('cost')
    plt.title(type)

    # display the plot
    plt.show()
