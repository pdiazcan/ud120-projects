#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]

"""
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()"""
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
from time import time
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

"""
# I'm going to try different values for n_estimators and learning_rate
#numEstimators = [50, 100, 150, 200]
#learningRate  = [0.1, 1]
numEstimators = [10, 50, 100, 150, 200, 250, 500, 750, 1000]
learningRate  = [0.01, 0.05, 0.1, 0.5, 0.75, 1, 1.25, 1.5, 2]
bestA = 0
bestE = 0
bestL = 0

for e in numEstimators:
    for l in learningRate:
        print('{} estimators, learning rate: {}'.format(e,l))
        # we define our classifier:
        clf = AdaBoostClassifier(n_estimators=e,
                                 learning_rate=l)
        
        # We train the classifier
        t0 = time()
        clf.fit(features_train, labels_train)
        print "training time:", round(time()-t0, 3), "s"
        
        # We predict from the test set
        pt0 = time()
        pred = clf.predict(features_test)
        print "prediction time:", round(time()-pt0, 3), "s"

        # We calculate the accuracy
        a = accuracy_score(pred, labels_test)
        print("accuracy:", a)
        
        if a > bestA: 
            print("new best! {} est and lea {}".format(e,l))      
            bestE = e
            bestL = l
            bestA = a
        else:
            print("The best is still {} est and lea {}".format(bestE,bestL))

# Best choice:
print('BEST CHOICE: {} estimators, learning rate: {}, accuracy: {}'.format(bestE,bestL, bestA))

e = bestE
l = bestL
"""
e = 150
l = 0.1
print("Best AdaBoost, {} estimators, {} learning rate".format(e,l))

# we define our classifier:
clf = AdaBoostClassifier(n_estimators=e,
                         learning_rate=l)

# We train the classifier
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# We predict from the test set
pt0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-pt0, 3), "s"

# We calculate the accuracy
print("accuracy:", accuracy_score(pred, labels_test))

# I'm going to try others:------------------------------------------------------------
"""from sklearn.neighbors import KNeighborsClassifier

for n in range(1,10):
    for l in range(1,50):
        print("{} Neighbors, {} leaf size".format(n,l))
        # we define our classifier:
        clf = KNeighborsClassifier(n_neighbors=n,
                                   weights='distance', 
                                   algorithm='auto', 
                                   leaf_size=l, 
                                   p=2, 
                                   metric='minkowski', 
                                   metric_params=None, 
                                   n_jobs=1)
        
        # We train the classifier
        t0 = time()
        clf.fit(features_train, labels_train)
        print "training time:", round(time()-t0, 3), "s"
        
        # We predict from the test set
        pt0 = time()
        pred = clf.predict(features_test)
        print "prediction time:", round(time()-pt0, 3), "s"
        
        # We calculate the accuracy
        print("accuracy:", accuracy_score(pred, labels_test))"""

# OK, Best KNN:
from sklearn.neighbors import KNeighborsClassifier
n = 10
l = 10
print("Best KKN, {} Neighbors, {} leaf size  = ".format(n,l))
# we define our classifier:
clf = KNeighborsClassifier(n_neighbors=n,
                           weights='distance', 
                           algorithm='kd_tree', 
                           leaf_size=l)

# We train the classifier
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# We predict from the test set
pt0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-pt0, 3), "s"

# We calculate the accuracy
print("accuracy:", accuracy_score(pred, labels_test))


# And now Random Forest:
from sklearn.ensemble import RandomForestClassifier
e = 2500
c = "entropy"
m = 150
l = 1

print("Best RandomForest, {} estimators, {} criterion, min_samples_split={}, min_samples_leaf={}".format(e,c,m,l))

# we define our classifier:
clf = RandomForestClassifier(n_estimators = e,
                             criterion = c,
                             min_samples_split = m,
                             min_samples_leaf = l)

# We train the classifier
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

# We predict from the test set
pt0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-pt0, 3), "s"

# We calculate the accuracy
print("accuracy:", accuracy_score(pred, labels_test))



try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
