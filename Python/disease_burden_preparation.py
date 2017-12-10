#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:52:22 2017

@author: yuchenli
@content: MarketScan exploration project, compile disease burden/prevalence and
          total cost
"""

import csv 
import time
import random


# Check the number of patients from ccaeo063 where client_id = 27 and dxcat = 
# RES05
with open('/Users/yuchenli/Box Sync/Yuchen_project/'
          'MarketScan_exploration_project/Data/'
          'Disease_burden_cluster_2006_2015/ccaeo063_sample.csv', \
          "w") as csvfile:
    writer0 = csv.writer(csvfile)
    
    snippet0 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                'Disease_burden_cluster_2006_2015/ccaeo063.csv')

    reader0 = csv.reader(snippet0)

    i=0
        
    for row in reader0:
        if (i%1000000==0):
            print(i)
        dxcat = str(row[0])
        client_id = str(row[1])
        
        if (client_id == '127' and dxcat == 'RES05'):
            writer0.writerow(row)
        i+=1
 
   
snippet0 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                'MarketScan_exploration_project/Data/'
                'Disease_burden_cluster_2006_2015/ccaeo133.csv')


# Measure the number of rows without enrolid
reader0 = csv.reader(snippet0)
empty_enrolid = 0
not_empty_enrolid = 0
i=0
for row in reader0:
    enrolid = str(row[2])
    if(i % 1000000 == 0):
        print(i)
    if(enrolid == ''):
        empty_enrolid+=1
    else:
        not_empty_enrolid+=1
    i+=1
# Conclusion: 236176 empty enrolid + 272723735 non-empty ones


# Compile disease prevalence and average cost
def prevalance_cost(df, outputname):
    snippet1 = open('/Users/yuchenli/Box Sync/Yuchen_project/'
                    'MarketScan_exploration_project/Data/'
                    'Disease_burden_cluster_2006_2015/' + df + '.csv')

    reader1 = csv.reader(snippet1)

    client = dict()
    i=0
    start_time = time.time()

    for row in reader1:
        if (i==0):
            i+=1
            continue
        if (i % 1000000 == 0):
            print(i)
        
        dxcat = str(row[0])
        client_id = str(row[1])
        enrolid = str(row[2])
        netpay = float(row[5])
        
        if (enrolid == ''):
            i+=1
            continue
        
        i+=1
            
        if (client_id not in client):
            client[client_id] = {'client_id': client_id,
                                 'enrolid_dxcat': set([enrolid + ":" + dxcat]),
                                 'enrolid': set([enrolid]),
                                 'count' : 0
                                 }
            if dxcat == 'END05':
                client[client_id]['END05'] = 1
                client[client_id]['END05_pay'] = netpay
                client[client_id]['count'] += 1                
            else:
                client[client_id]['END05'] = 0
                client[client_id]['END05_pay'] = 0
                
            if dxcat =='CVS09':
                client[client_id]['CVS09'] = 1
                client[client_id]['CVS09_pay'] = netpay
                client[client_id]['count'] += 1 
            else:
                client[client_id]['CVS09'] = 0
                client[client_id]['CVS09_pay'] = 0
                
            if dxcat == 'RES02':
                client[client_id]['RES02'] = 1
                client[client_id]['RES02_pay'] = netpay
                client[client_id]['count'] += 1 
            else:
                client[client_id]['RES02'] = 0
                client[client_id]['RES02_pay'] = 0   
                
            if dxcat == 'RES05':
                client[client_id]['RES05'] = 1
                client[client_id]['RES05_pay'] = netpay
                client[client_id]['count'] += 1 
            else:
                client[client_id]['RES05'] = 0
                client[client_id]['RES05_pay'] = 0
                
        else: # if client_id in client already
        
            if (enrolid + ":" + dxcat) not in client[client_id]['enrolid_dxcat']:
                client[client_id]['enrolid_dxcat'].add(enrolid + ":" + dxcat)
                if dxcat == 'END05':
                    client[client_id]['END05'] += 1
                    client[client_id]['END05_pay'] += netpay
            
                if dxcat =='CVS09':
                    client[client_id]['CVS09'] += 1
                    client[client_id]['CVS09_pay'] += netpay
    
                if dxcat == 'RES02':
                    client[client_id]['RES02'] += 1
                    client[client_id]['RES02_pay'] += netpay
                    
                if dxcat == 'RES05':
                    client[client_id]['RES05'] += 1
                    client[client_id]['RES05_pay'] += netpay 
                                
            else: # if enrolid in client[client_id]['enrolid']
            
                if dxcat == 'END05':                
                    client[client_id]['END05_pay'] += netpay
            
                if dxcat =='CVS09':
                    client[client_id]['CVS09_pay'] += netpay
    
                if dxcat == 'RES02':
                    client[client_id]['RES02_pay'] += netpay
                    
                if dxcat == 'RES05':
                    client[client_id]['RES05_pay'] += netpay 
            
            if (enrolid not in client[client_id]['enrolid']):
                client[client_id]['enrolid'].add(enrolid)
                client[client_id]['count'] += 1
            
    print("--- %s seconds ---" % (time.time() - start_time))    
    
    
    with open('/Users/yuchenli/Box Sync/Yuchen_project/'
              'MarketScan_exploration_project/Data/'
              'Disease_burden_cluster_2006_2015/' + outputname + '.csv',
              "w") as csvfile:
        fieldnames = ['client', "END05","END05_pay","CVS09", "CVS09_pay",\
                      'RES02', 'RES02_pay', 'RES05', 'RES05_pay', 'count']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        for key in client:
            writer.writerow({'client': key, 
                             "END05": client[key]['END05'],
                             "END05_pay": client[key]['END05_pay'],
                             "CVS09": client[key]['CVS09'], 
                             "CVS09_pay": client[key]['CVS09_pay'],
                             'RES02': client[key]['RES02'], 
                             'RES02_pay': client[key]['RES02_pay'], 
                             'RES05': client[key]['RES05'], 
                             'RES05_pay': client[key]['RES05_pay'], 
                             'count': client[key]['count']})
   

prevalance_cost('ccaeo063', '2006')
prevalance_cost('ccaeo073', '2007')
prevalance_cost('ccaeo083', '2008')
prevalance_cost('ccaeo093', '2009')
prevalance_cost('ccaeo103', '2010')
prevalance_cost('ccaeo113', '2011')
prevalance_cost('ccaeo123', '2012')
prevalance_cost('ccaeo133', '2013')
prevalance_cost('ccaeo143', '2014')
prevalance_cost('ccaeo152', '2015')

