# Supervised Learning - learning from provided examples

# In machine learning, often extract features and try to produce labels

# Common question in Machine Learning:
# What can we say about a new data point that we've never seen before given past data?

# Decision surface linear - a line to different types of points on a scatter plot
# red cross vice blue circle, for instance.

# Naive Bayes - common algorithm to find a decision surface

# import numpy as np
#
# # Features
# X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
# # Labels
# Y = np.array([1, 1, 1, 2, 2, 2])
#
# from sklearn.naive_bayes import GaussianNB
# from sklearn.metrics import accuracy_score
#
# clf = GaussianNB()
# # classify a fit for (features, labels)
# clf.fit(X, Y)
# GaussianNB()
#
# prediction = clf.predict([[-0.8, -1]])
# print(prediction)
#
# # accuracy = number of points classified correctly / all points (in test set)
# # use sklearn.metrics.accuracy_score
#
# # Always train and test on different data sets.
# # Save ~10% of data to be used for testing, don't feed this into the learning set.
#
# # Bayes Rule - The Holy Grail of probabilistic inference.
# # Fun fact: Rev Thomas Bayes used this principle to infer the existence of god
#
# # An example:
# # The probability P that a person has this specific cancer C is P(C) = 0.01
# # 90% of positive tests indicating that a person has C are accurate, this is the sensitivity.
# # 10% of positive tests are false positives.
# # 90% of negative tests are accurate if you don't have C. This is called the specificity
#
# # Bayes Rule:
# # prior probability with incorporated test evidence leads to a posterior probability
# #
# # prior:    P(C) = 0.01 = 1%
# #           P(Pos|C) = 0.9 = 90%
# #           P(!C) = 0.99 = 99%
# #           P(Neg|!C) = 0.9 = 90%
# #           P(Pos|!C) = 0.1 = 10%
#
# # posterior: P(C|Pos.) = P(C) * P(Pos|C) = 0.009
# # posterior: P(!C|Pos.) = P(!C) * P(Pos|!C) = 0.099
# # posterior also called joint probability of events
#
# # normalization, 2 steps: keep ratio same but make sure they add to 1.
# p1 = 0.009
# p2 = 0.099
# # normalizer: P(Pos) = P(C, Pos) + P(!C, Pos) = 0.108
# normalizer = p1 + p2
# print(p1 / normalizer)
# # P(C|Pos) = 0.0833
# print(p2 / normalizer)
# # P(!C|Pos) = 0.9167
#
# print((p1 + p2) / normalizer)
# # 1
#
# # Bayes Rule used often for Text Learning, which is learning from documents
# # Also called Naive Bayes - Bayesian Probabilities
#
# pC = 0.5
# pS = 0.5
#
# ldC = pC * .8 * .1
# ldS = pS * .5 * .2
#
# normalizer = ldC + ldS
# print(ldC / normalizer)
# print(ldS / normalizer)



# SVMs - Support Vector Machines
# SVMs find a separating line called a hyperplane between data of two different classes.
# The SVM algorithm takes as input this data of two different classes and outputs the line

# First and foremost, get the classification correctly. Subject to this constraint,
# should attempt to maximize the distance to the nearest points of either class (the margin)
# Extreme outliers are tolerable, can be ignored, SVM is somewhat robust to these outliers

from sklearn import svm
from sklearn.metrics import accuracy_score


X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
# SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
#     decision_function_shape=None, degree=3, gamma='auto', kernel='rbf',
#     max_iter=-1, probability=False, random_state=None, shrinking=True,
#     tol=0.001, verbose=False)

print(clf.predict([[2., 2.]]))

# SVM with Nonlinear Data
# for a case where class 1 clusters around origin and class 2 is dotted all around
# z = x^2 + y^2 allows us encircle the class 1 data in the center
# to build a new graph, one where class 2 always has a
# higher z value than class 1, and now we can draw a line.

# We can add another feature, too. Take the absolute value of one of the coordinates,
# if it makes sense with the data.

# The Kernel Trick
# There are functions that take a low dimensional feature space (x,y)
# And map it to a very high dimensional space (xsub1, xsub2, xsub3, xsub4, xsub5)
# And turn what was not a separable dataset into a separable one. These functions
# are called kernels. We get a solution with the SVM using the kernel trick, and end
# up with a nonlinear separation











# Support Vector Machines


# Selecting a Supervised Classification Algorithm:
# Naive Bayes - very easy to implement, very efficient to run
# - dangers: Phrases that encompass multiple words don't do well, can't handle word order
# SVMs - Support Vector Machines -

