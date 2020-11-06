#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 14:51:47 2020

"""

import os
import glob
import pandas as pd
os.chdir("/Users/INSERT PATH HERE")
extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "InsertNAMEcombined.csv", index=False, encoding='utf-8-sig')