#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC

# OK, we're slicing the training set to only 1% of the original training set...
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

# ok, now we're going to use a rbf kernel, instead of linear...
# clf = SVC(kernel = "linear")
clf = SVC(kernel = "rbf",
          C = 10000)

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

"""
# Now we're going to try differents parameters...
# try several values of C (say, 10.0, 100., 1000., and 10000.)
C = [10, 100, 1000, 10000]

for c in C:
    print("Testing C = ", c)
    # ok, now we're going to use a rbf kernel, instead of linear...
    # clf = SVC(kernel = "linear")
    clf = SVC(kernel = "rbf",
              C = c)
    
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
"""    
#########################################################


