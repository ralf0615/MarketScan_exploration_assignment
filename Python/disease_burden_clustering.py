#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:19:33 2017

@author: yuchenli
@content: disease burden clustering
"""

import pandas as pd
import csv

def read_burden(df, name):
    exec(name + " = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/" +
                "MarketScan_exploration_project/Data/" + 
                "Disease_burden_cluster_2006_2015/" + df + ".csv')")

read_burden('2006', 'b_2006')
b_2006 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2006.csv')
read_burden('2007', 'b_2007')
b_2007 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2007.csv')
read_burden('2008', 'b_2008')
b_2008 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2008.csv')
read_burden('2009', 'b_2009')
b_2009 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2009.csv')
read_burden('2010', 'b_2010')
b_2010 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2010.csv')
read_burden('2011', 'b_2011')
b_2011 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2011.csv')
read_burden('2012', 'b_2012')
b_2012 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2012.csv')
read_burden('2013', 'b_2013')
b_2013 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2013.csv')
read_burden('2014', 'b_2014')
b_2014 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2014.csv')
read_burden('2015', 'b_2015')
b_2015 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                     'MarketScan_exploration_project/Data/' 
                     'Disease_burden_cluster_2006_2015/2015.csv')


#==============================================================================
# def compile_disease(df1, df2, name):
#     burden = dict()
#     for i in range(len(df1)):
#         client = df1.iloc[i,2]
#         disease = df1.iloc[i,1]
#         value = df1.iloc[i,0]
#         if client not in burden:
#             burden[client] = {}
#             if (disease == 'END05'):
#                 burden[client]['END05'] = value
#             if (disease == 'RES02'):
#                 burden[client]['RES02'] = value    
#             if (disease == 'CVS09'):
#                 burden[client]['CVS09'] = value    
#             if (disease == 'RES05'):
#                 burden[client]['RES05'] = value
#         else:
#             if (disease == 'END05'):
#                 burden[client]['END05'] = value
#             if (disease == 'RES02'):
#                 burden[client]['RES02'] = value    
#             if (disease == 'CVS09'):
#                 burden[client]['CVS09'] = value    
#             if (disease == 'RES05'):
#                 burden[client]['RES05'] = value
# 
#     pay = dict()
#     for i in range(len(df2)):
#         client = df2.iloc[i,1]
#         disease = df2.iloc[i,2]
#         value = df2.iloc[i,0]
#         if client not in pay:
#             pay[client] = {}
#             if (disease == 'END05'):
#                 pay[client]['END05'] = value
#             if (disease == 'RES02'):
#                 pay[client]['RES02'] = value    
#             if (disease == 'CVS09'):
#                 pay[client]['CVS09'] = value    
#             if (disease == 'RES05'):
#                 pay[client]['RES05'] = value
#         else:
#             if (disease == 'END05'):
#                 pay[client]['END05'] = value
#             if (disease == 'RES02'):
#                 pay[client]['RES02'] = value    
#             if (disease == 'CVS09'):
#                 pay[client]['CVS09'] = value    
#             if (disease == 'RES05'):
#                 pay[client]['RES05'] = value
#     
#     with open('/Users/yuchenli/Box Sync/Yuchen_project/'
#               'MarketScan_exploration_project/Data/'
#               'Disease_burden_cluster_2013_2015/' + name, \
#               "w") as csvfile:
#         fieldnames = ['client', "END05","END05_pay","CVS09", "CVS09_pay",\
#                       'RES02', 'RES02_pay', 'RES05', 'RES05_pay']
#         writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
#         writer.writeheader()
#         for key in burden:
#             writer.writerow({'client': key, 
#                              "END05": burden[key]['END05'],
#                              "END05_pay": pay[key]['END05'],
#                              "CVS09": burden[key]['CVS09'], 
#                              "CVS09_pay": pay[key]['CVS09'],
#                              'RES02': burden[key]['RES02'], 
#                              'RES02_pay': pay[key]['RES02'], 
#                              'RES05': burden[key]['RES05'], 
#                              'RES05_pay': pay[key]['RES05']})
# 
# compile_disease(burden_2013, netpay_2013, 'result_2013.csv')
# compile_disease(burden_2014, netpay_2014, 'result_2014.csv')
# compile_disease(burden_2015, netpay_2015, 'result_2015.csv')
#==============================================================================

# Compile average cost and disease prevalence
    
def compile_2(df):
    general = dict()
    for i in range(len(df)):
        client = df.iloc[i,0]
        count = df.iloc[i,9]
        END05 = df.iloc[i,1]/count
        if END05 == 0:
            END05_pay = df.iloc[i,2]
        else:
            END05_pay = df.iloc[i,2]/df.iloc[i,1]
        
        CVS09 = df.iloc[i,3]/count
        if CVS09 == 0:
            CVS09_pay = df.iloc[i,4]
        else:
            CVS09_pay = df.iloc[i,4]/df.iloc[i,3]
            
        RES02 = df.iloc[i,5]/count
        if RES02 == 0:
            RES02_pay = df.iloc[i,6]
        else:
            RES02_pay = df.iloc[i,6]/df.iloc[i,5]

        RES05 = df.iloc[i,7]/count
        if RES05 == 0:
            RES05_pay = df.iloc[i,8]
        else:
            RES05_pay = df.iloc[i,8]/df.iloc[i,7]
        
        general[client] = {'client': client, 
                           'count': count,
                           "END05": END05,
                           "END05_pay": END05_pay,
                           "CVS09": CVS09, 
                           "CVS09_pay": CVS09_pay,
                           'RES02': RES02, 
                           'RES02_pay': RES02_pay, 
                           'RES05': RES05, 
                           'RES05_pay': RES05_pay}
    return general

c_2006 = compile_2(b_2006)
c_2007 = compile_2(b_2007)
c_2008 = compile_2(b_2008)
c_2009 = compile_2(b_2009)
c_2010 = compile_2(b_2010)
c_2011 = compile_2(b_2011)
c_2012 = compile_2(b_2012)
c_2013 = compile_2(b_2013)
c_2014 = compile_2(b_2014)
c_2015 = compile_2(b_2015)

# Convert dict to data frame
d_2006 = pd.DataFrame.from_dict(c_2006, orient = 'index')
d_2007 = pd.DataFrame.from_dict(c_2007, orient = 'index')
d_2008 = pd.DataFrame.from_dict(c_2008, orient = 'index')
d_2009 = pd.DataFrame.from_dict(c_2009, orient = 'index')
d_2010 = pd.DataFrame.from_dict(c_2010, orient = 'index')
d_2011 = pd.DataFrame.from_dict(c_2011, orient = 'index')
d_2012 = pd.DataFrame.from_dict(c_2012, orient = 'index')
d_2013 = pd.DataFrame.from_dict(c_2013, orient = 'index')
d_2014 = pd.DataFrame.from_dict(c_2014, orient = 'index')
d_2015 = pd.DataFrame.from_dict(c_2015, orient = 'index')


# Clustering

## Read in client name
import pandas as pd

client_name = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                          'MarketScan_exploration_project/Data/'
                          '/Client_name/2013_client_standard.csv')
client_name_dict = dict()
for i in range(len(client_name)):
    key = client_name.iloc[i,0].split(" ")[0]
    value = client_name.iloc[i,0].split(" ")[1]
    client_name_dict[key] = value


#result_2013 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
#                          'MarketScan_exploration_project/Data/'
#                          'Disease_burden_cluster_2013_2015/result_2013.csv')
#result_2014 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
#                          'MarketScan_exploration_project/Data/'
#                          'Disease_burden_cluster_2013_2015/result_2014.csv')
#result_2015 = pd.read_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
#                          'MarketScan_exploration_project/Data/'
#                          'Disease_burden_cluster_2013_2015/result_2015.csv')

def quadrant(disease,pay):
    if (disease > 0 and pay > 0):
        return 'high prevalence/high cost'
    elif (disease < 0 and pay > 0):
        return 'low prevalence/high cost'
    elif (disease < 0 and pay < 0):
        return 'low prevalence/low cost'
    else:
        return 'high prevalence/low cost'
    
client_industry = dict({'': 'Missing',
                       '1': 'Oil & Gas Extraction, Mining',                       
                       '2': 'Manufacturing, Durable Goods',                     
                       '3': 'Manufacturing, Nondurable Goods',                  
                       '4': 'Transportation, Communications, Utilities',         
                       '5': 'Retail Trade',                                    
                       '6': 'Finance, Insurance, Real Estate',                 
                       '7': 'Services',                                      
                       'A': 'Agriculture, Forestry, Fishing',                     
                       'C': 'Construction',                                      
                       'W': 'Wholesale'})                                       
 
def standard(df, name, year):
    from sklearn import preprocessing
    client = df.iloc[:,0]
    df = df.iloc[:,2:10]
    
    year = str(year)

    df_std = preprocessing.scale(df)
    temp = pd.DataFrame(df_std)
    list_1 = list()
    list_2 = list()
    list_3 = list()
    list_4 = list()
    list_5 = list()
    list_6 = list()
    
    for i in range(len(temp)):
        end05 = temp.iloc[i,0]
        end05_pay = temp.iloc[i,1]
        cvs09 = temp.iloc[i,2]
        cvs09_pay = temp.iloc[i,3]
        res02 = temp.iloc[i,4]
        res02_pay = temp.iloc[i,5]
        res05 = temp.iloc[i,6]
        res05_pay = temp.iloc[i,7]
        
        list_1.append(quadrant(end05, end05_pay))
        list_2.append(quadrant(cvs09, cvs09_pay))
        list_3.append(quadrant(res02, res02_pay))
        list_4.append(quadrant(res05, res05_pay))
        
    for element in client:
        list_5.append(str(element) + "_" + client_name_dict[str(element)])
        list_6.append(client_industry[industry_dict[str(element)][0]])

      
    list_combine = pd.DataFrame({'END05/pay_' + year: list_1, 
                                 'CVS09/pay_' + year: list_2, 
                                 'RES02/pay_' + year: list_3, 
                                 'RES05/pay_' + year: list_4,
                                 'Client': list_5,
                                 'Industry': list_6})
    list_combine.to_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                        'MarketScan_exploration_project/Data/'
                        'Disease_burden_cluster_2006_2015/' + name + '_quadrant.csv',
                        index = False)
    temp.to_csv('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                'Disease_burden_cluster_2006_2015/' + name + '.csv')
    
standard(d_2006, "2006_std", 2006)
standard(d_2007, "2007_std", 2007)
standard(d_2008, "2008_std", 2008)
standard(d_2009, "2009_std", 2009)
standard(d_2010, "2010_std", 2010)
standard(d_2011, "2011_std", 2011)
standard(d_2012, "2012_std", 2012)
standard(d_2013, "2013_std", 2013)
standard(d_2014, "2014_std", 2014)
standard(d_2015, "2015_std", 2015)

