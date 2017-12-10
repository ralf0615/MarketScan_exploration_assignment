#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:49:27 2017

@author: yuchenli
@content: exploration
          compile shared clients over the years
"""

import math
import statistics
import csv
import time
import pandas as pd


# Count the number of rows in ccaeo123.csv
snippet4 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                'Disease_burden_cluster_2006_2015/ccaeo123.csv')
reader4 = csv.reader(snippet4)

i=0
j=0
patient_id_list = set()

for row in reader4:
    if (i % 1000000 == 0):
        print(i)
    patient_id = str(row[2])
    if patient_id not in patient_id_list:
        patient_id_list.add(patient_id)
        j+=1
    i+=1
    

# Create CPT_dict
snippet1 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/Essential Dict/'
                'cpt_table.csv', encoding = "ISO-8859-1")
reader1 = csv.reader(snippet1)

CPT_dict = dict()
i=0

for row in reader1:
    if (i==0):
        i+=1
        continue
    i+=1
    key = "b:" + str(row[0])
    trash1 = dict()
    value1 = str(row[1])
    value2 = str(row[2])
    trash1["Short_text"] = value1
    trash1["Long_text"] = value2
    
    CPT_dict[key] = trash1
    

# Create ICD9_dict
snippet2 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/Essential Dict/'
                'icd9.csv', encoding = "ISO-8859-1")
reader2 = csv.reader(snippet2)

ICD9_dict = dict()
i=0

for row in reader2:
    if (i==0):
        i+=1
        continue
    i+=1
    key = "b:" + str(row[0])
    trash1 = dict()
    value1 = str(row[2])
    value2 = str(row[3])
    trash1["Short_text"] = value1
    trash1["Long_text"] = value2
    
    ICD9_dict[key] = trash1
    


# Create ICD10_dict
snippet3 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/Essential Dict/'
                'icd10.csv', encoding = "ISO-8859-1")
reader3 = csv.reader(snippet3)

ICD10_dict = dict()
i=0

for row in reader3:
    if (i==0):
        i+=1
        continue
    i+=1
    key = "b:" + str(row[1])
    trash1 = dict()
    value1 = str(row[4])
    value2 = str(row[5])
    trash1["Short_text"] = value1
    trash1["Long_text"] = value2
    
    ICD10_dict[key] = trash1
    

# Read clients from 2006 to 2015
client_2013 = dict()
snippet4 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2013_client.csv')
reader4 = csv.reader(snippet4)
for row in reader4:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2013[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2013_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2013.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass
        
    
client_2014 = dict()
snippet5 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2014_client.csv')
reader5 = csv.reader(snippet5)
for row in reader5:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2014[key] = value

with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2014_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2014.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass
    
    
client_2015 = dict()
snippet6 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2015_client.csv')
reader6 = csv.reader(snippet6)
for row in reader6:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2015[key] = value

with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2015_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2015.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass
        
client_2012 = dict()
snippet7 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2012_client.csv')
reader7 = csv.reader(snippet7)
for row in reader7:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2012[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2012_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2012.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass    
        
client_2011 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2011_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2011[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2011_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2011.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass   
        
client_2010 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2010_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2010[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2010_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2010.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass          

client_2009 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2009_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2009[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2009_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2009.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass   
        
client_2008 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2008_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2008[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2008_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2008.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass   
        
client_2007 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2007_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2007[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2007_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2007.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass  
        
client_2006 = dict()
snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                '2006_client.csv')
reader8 = csv.reader(snippet8)
for row in reader8:
    key = row[0][27:45].strip()
    value = row[0][46:58]
    client_2006[key] = value
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          '2006_client_standard.csv', "w") as csvfile:
    fieldnames = ['client', "count"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for key, value in client_2006.items():
        try:
            writer.writerow({'client': key, "count": value})
        except:
            pass 
        
# Find common client from 2006-2015
shared_client = list()
unique_client = list()
for key in client_2013:
    if (key in client_2014 and key in client_2015 and key in client_2012\
        and key in client_2011 and key in client_2010 and key in client_2009
        and key in client_2008 and key in client_2007 and key in client_2006):
        shared_client.append(key)
        print(key)
    else:
        unique_client.append(key)
    
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          'shared_client_2006_2015.csv', "w") as csvfile:
    fieldnames = ['client', "count_2006", "count_2007", 
                  "count_2008", 
                  "count_2009", "count_2010", 
                  "count_2011","count_2012",
                  "count_2013", "count_2014", "count_2015"]
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    for element in shared_client:
        try:
            writer.writerow({'client': element, 
                             "count_2006": client_2006[element],
                             "count_2007": client_2007[element],
                             "count_2008": client_2008[element],
                             "count_2009": client_2009[element],
                             "count_2010": client_2010[element],
                             "count_2011": client_2011[element],
                             "count_2012": client_2012[element],
                             "count_2013": client_2013[element],
                             "count_2014": client_2014[element],
                             "count_2015": client_2015[element]})
        except:
            pass

        
# Print out shared client for SAS code
client_string = ""
for client in shared_client:
    print(client.split(" ")[0])
    client_string = client_string + client.split(" ")[0] + ","
    
        
## Read shared_client_2013_2015_filtered
#snippet8 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
#                'MarketScan_exploration_project/Data/'
#                'shared_client_2013_2015_filtered.csv')
#reader8 = csv.reader(snippet8)
#i=1
#for row in reader8:
#    i+=1
#    print(row[0][0:4])
#print("There are", i, "rows")


# Match client with industry
snippet9 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                'Disease_burden_cluster_2006_2015/ccaeo133.csv')
reader9 = csv.reader(snippet9)
i=0
industry_dict = dict()

for row in reader9:
    if(i%1000000==0):
        print(i)
    i+=1
    client = row[1]
    industry = row[3]
    if client not in industry_dict:
        industry_dict[client] = list(industry)            
    else:
        try:
            if industry not in industry_dict[client]:
                industry_dict[client].append(industry)
        except:
                industry_dict[client].append("NA")
        
    