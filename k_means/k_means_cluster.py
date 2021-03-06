#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_3 = "total_payments"

poi  = "poi"
#features_list = [poi, feature_1, feature_2, feature_3]
features_list = [poi, feature_1, feature_2]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
finance_features_bk = numpy.array(finance_features)
finance_features = numpy.array(finance_features)
salary = finance_features[:,0]
ex_stok = finance_features[:,1]
salary = [min(salary),200000.0,max(salary)]
ex_stok = [min(ex_stok),1000000.0,max(ex_stok)]
rescaled_salary = scaler.fit_transform(salary)
rescaled_stock = scaler.fit_transform(ex_stok)
print "salary: ", rescaled_salary
print "exercised_stock_options: ", rescaled_stock

finance_features[:,0] = scaler.fit_transform(finance_features[:,0])
finance_features[:,1] = scaler.fit_transform(finance_features[:,1])


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
#for f1, f2, f3 in finance_features:
for f1, f2 in finance_features:
    plt.scatter( f1, f2 )
plt.show()

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
from sklearn.cluster import KMeans
clu = KMeans(n_clusters=2)
clu.fit(finance_features, poi)
pred = clu.predict(finance_features)

### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters2.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"


# searching for max and min in a feature:
from pprint import pprint
exercised_stock_options = []
for key in data_dict:
    val = data_dict[key]['exercised_stock_options']
    if val == 'NaN':
        continue
    exercised_stock_options.append((key,int(val)))

print("Max and Min exercised_stock_options")
pprint(sorted(exercised_stock_options,key=lambda x:x[1],reverse=True)[:4])
pprint(sorted(exercised_stock_options,key=lambda x:x[1],reverse=False)[:4])

from pprint import pprint
salary = []
for key in data_dict:
    val = data_dict[key]['salary']
    if val == 'NaN':
        continue
    salary.append((key,int(val)))

print("Max and Min salary")
pprint(sorted(salary,key=lambda x:x[1],reverse=True)[:4])
pprint(sorted(salary,key=lambda x:x[1],reverse=False)[:4])