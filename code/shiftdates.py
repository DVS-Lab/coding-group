#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : David Smith
# Created Date: Mon Sep 6 2021
# =============================================================================
'''
This code shifts the dates in the acq_time column of the scans.tsv files. It takes
the bids folder as its input, finds all of the tsv files, and shift the dates.

usage:
python3 shiftdates.py /data/projects/istart-data/bids/

notes and disclaimers:
0) should only be run once a bids data set (otherwise you shift again)
1) needs trailing slash on input path
2) supressing a performancewarning right now, so code could definitely be improved
3) overwrites input data. not sure where else to dump it.
'''

# =============================================================================
# Imports
# =============================================================================
import glob
import sys
import datetime, dateutil
import pandas as pd


# =============================================================================
# To do's and things to improve
# This is intended to supress the following warning that i was getting:
# /fakepath/datetimelike.py:1187: PerformanceWarning: Adding/subtracting object-dtype array to DatetimeArray not vectorized
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)
# =============================================================================



# make list of tsvs
scans = glob.glob(sys.argv[1] + 's*/**scans.tsv', recursive = True)
msg = 'found %d scan tsv file' % len(scans)
print(msg)

# loop through all scan tsv files
for scan in scans:

    # print out progress and load in tsv file
    print('scrubbing ' + scan)
    df = pd.read_csv(scan, sep = '\t')

    # convert string to datetime format and create datetime object for relative time in tmp
    df['acq_time'] = pd.to_datetime(df['acq_time'],infer_datetime_format=True)
    df['tmp'] = dateutil.relativedelta.relativedelta(months=100*12) # shift date by 100 years. needs to be < 1925

    # shift the dates, drop tmp column, and convert back to string format
    df['acq_time'] = df['acq_time'] - df['tmp']
    df.drop(columns = ['tmp'],axis=1,inplace=True)
    df['acq_time'] = df['acq_time'].dt.strftime('%Y-%m-%dT%H:%M:%S.%f')

    # edit operator column so that it doesn't output as empty
    df['operator'] = 'tubric'

    # save revised dataframe. overwrites existing!
    df.to_csv(scan, sep = '\t', index = False)