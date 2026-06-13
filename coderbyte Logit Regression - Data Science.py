"""
mediumDiscussion Solutions 
Logit Regression Problem

Have the function LogitRegression(arr) read the input array of 4 numbers x, y, a, b, separated by space, and return an output of two numbers for updated a and b (assume the learning rate is 1). Save up to 3 digits after the decimal points for a and b. The output should be a string in the format: a, b

Logistic regression is a simple approach to do classification, and the same formula is also commonly used as the output layer in neural networks. We assume both the input and output variables are scalars, and the logistic regression can be written as:

y = 1.0 / (1.0 + exp(-ax - b))

After observing a data example (x, y), the parameter a and b can be updated using gradient descent with a learning rate.
Examples
Input: [1, 1, 1, 1]
Output: 0.881, 0.881
Input: [2.2, 0.0, 5.1, 5.7]
Output: 7.3, 6.7
Tags
arraystatisticsdata sciencemachine learning
"""
arr = [1, 1, 1, 1] # Output: 0.881, 0.881
arr = [2.2, 0.0, 5.1, 5.7] # Output: 7.3, 6.7

def LogitRegression(arr):

    import numpy as np
    x,y,a,b = arr[0], arr[1], arr[2], arr[3] 
    # for _ in range(10000):
    y_hat = 1.0 / (1.0 + np.exp(-a*x - b))

    delta = y - y_hat
    learning_rate = 1.0
    # a_new = a - learning_rate * delta*x
    # b_new = b - learning_rate * delta

    a_new = round((a - learning_rate*delta*x), 3)
    b_new = round((b - learning_rate*delta), 3)
    

    return str(a_new), str(b_new)

LogitRegression(arr)