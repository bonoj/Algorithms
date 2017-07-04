# Supervised Learning - learning from provided examples

# In machine learning, often extract features and try to produce labels

# Common question in Machine Learning:
# What can we say about a new data point that we've never seen before given past data?

# Decision surface linear - a line to different types of points on a scatter plot
# red cross vice blue circle, for instance.

# Naive Bayes - common algorithm to find a decision surface

import numpy as np

# Features
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# Labels
Y = np.array([1, 1, 1, 2, 2, 2])

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
# classify a fit for (features, labels)
clf.fit(X, Y)
GaussianNB()
print(clf.predict([[-0.8, -1]]))

