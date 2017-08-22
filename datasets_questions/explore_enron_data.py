#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

""" how many poi are there?
poi = 0

for person in enron_data:
    if enron_data[person]["poi"] == 1 :
        poi += 1
        
print(poi)
"""

"""
print(enron_data["PRENTICE JAMES"]["total_stock_value"])
print(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])
print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])
"""

"""
max_money = 0
for person, i in enron_data.items():
    if (enron_data[person]["total_payments"] > max_money ) and (enron_data[person]["total_payments"] != "NaN" ):
        if person != "TOTAL":
            max_money = enron_data[person]["total_payments"]
            max_person = person
        # print(i)
        print(person)
        print(enron_data[person]["total_payments"])
        
print("{} : {}".format(max_person,max_money))
"""

"""
salary = 0

for person in enron_data:
    if enron_data[person]["salary"] != 'NaN' :
        salary += 1
        
print("People with quantified salary:", salary)

email_address = 0

for person in enron_data:
    if enron_data[person]["email_address"] != 'NaN' :
        email_address += 1
        
print("People with known email:", email_address)
"""

"""
missing_pay = 0
total = 0

for person in enron_data:
    total += 1
    if enron_data[person]["total_payments"] == 'NaN' :
        missing_pay += 1

perc = float(float(missing_pay) / float(total)) * 100
print(perc)
print("{} people with missing total payments. {} of the total {}".format(missing_pay, perc, total))
"""

missing_pay = 0
total = 0

for person in enron_data:
    if enron_data[person]["poi"] == True :
        total += 1
        if enron_data[person]["total_payments"] == 'NaN' :
            missing_pay += 1

perc = float(float(missing_pay) / float(total)) * 100
print(perc)
print("{} poi with missing total payments. {} of the total {}".format(missing_pay, perc, total))
