#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree

# OK, we're slicing the training set to only 1% of the original training set...
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

# we define our classifier:
clf = tree.DecisionTreeClassifier(min_samples_split=40)

# We train the classifier
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# We predict from the test set
pt0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-pt0, 3), "s"

# We calculate the accuracy
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, labels_test))

# some answers:
#print([pred[10], pred[26], pred[50]])

# Chris class... (y = 1)
print("Predicted as Chris: ", sum(pred))

#########################################################


