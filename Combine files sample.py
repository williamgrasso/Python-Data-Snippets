#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:07:45 2020

"""

import pandas as pd
import csv

f = open("/Users/INSERT PATH HERE.csv", 'r', encoding='utf-8')
reader = csv.reader(f, delimiter='\t')
for row in reader:
    row = row[0]
    read_file = pd.read_csv (r'/Users/INSERT PATH HERE./Group Project/gl1990_19/'+row+'.txt', header = None)
    read_file.columns = ['Insert','Column','Titles']
    read_file.to_csv('/Users/INSERT PATH HERE/Group Project/Master_File.csv', mode='a', header = False)
