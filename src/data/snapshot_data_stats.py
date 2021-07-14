# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:20:30 2021

Snapshot data and statistics script.
Uses snapshot_data_mod and the spreadsheet stored at \snapshot_pilot\SS_data_collector.xlsx,
which contains: list of mice/slides/slices obtained through snapshot pilot experiment, raw cell counts by slice, basic histology info,
and the 4OHT dosage the mouse received.

Green = gfp (eGFP)
Red = tom (tdTomato)

@author: dpaynter
"""
## Imports:
import snapshot_data_mod as ssd
import matplotlib.pyplot as plt
import numpy as np
import sys, os
import pandas as pd

date = str(input("What is today's date?"))

ss_dir = os.path.dirname(os.path.dirname(os.getcwd()))
datapath = ss_dir + r'\SS_data_collector.xlsx'
savefigpath = ss_dir + r'\reports\figures'


# Create an object for each mouse
DP_210202A = ssd.snapshot_mouse("DP_210202A", datapath)
DP_210202B = ssd.snapshot_mouse("DP_210202B", datapath)
DP_210202C = ssd.snapshot_mouse("DP_210202C", datapath)
DP_210202D = ssd.snapshot_mouse("DP_210202D", datapath)
DP_210203A = ssd.snapshot_mouse("DP_210203A", datapath)
DP_210203B = ssd.snapshot_mouse("DP_210203B", datapath)
DP_210308A = ssd.snapshot_mouse("DP_210308A", datapath)
DP_210308B = ssd.snapshot_mouse("DP_210308B", datapath)
DP_210308C = ssd.snapshot_mouse("DP_210308C", datapath)
DP_210416A = ssd.snapshot_mouse("DP_210416A", datapath)
DP_210416B = ssd.snapshot_mouse("DP_210416B", datapath)
DP_210417 = ssd.snapshot_mouse("DP_210417", datapath)

# Make a dataframe to be used for analyses
df = pd.DataFrame({'mouse': ['DP_210202A','DP_210202B','DP_210202C','DP_210202D','DP_210203A', 'DP_210203B',
                             'DP_210308A', 'DP_210308B', 'DP_210308C', 'DP_210416A', 'DP_210416B', 'DP_210417'],
                   'gfp_prop': [DP_210202A.green_only_prop, DP_210202B.green_only_prop,
                                DP_210202C.green_only_prop, DP_210202D.green_only_prop,
                                DP_210203A.green_only_prop, DP_210203B.green_only_prop,
                                DP_210308A.green_only_prop, DP_210308B.green_only_prop, 
                                DP_210308C.green_only_prop, DP_210416A.green_only_prop, 
                                DP_210416B.green_only_prop, DP_210417.green_only_prop],
                   'tom_prop': [DP_210202A.red_only_prop, DP_210202B.red_only_prop,
                                DP_210202C.red_only_prop, DP_210202D.red_only_prop,
                                DP_210203A.red_only_prop, DP_210203B.red_only_prop,
                                DP_210308A.red_only_prop, DP_210308B.red_only_prop, 
                                DP_210308C.red_only_prop, DP_210416A.red_only_prop, 
                                DP_210416B.red_only_prop, DP_210417.red_only_prop],
                   'condition': [DP_210202A.condition4OHT, DP_210202B.condition4OHT,
                                DP_210202C.condition4OHT, DP_210202D.condition4OHT,
                                DP_210203A.condition4OHT, DP_210203B.condition4OHT,
                                DP_210308A.condition4OHT, DP_210308B.condition4OHT, 
                                DP_210308C.condition4OHT, DP_210416A.condition4OHT, 
                                DP_210416B.condition4OHT, DP_210417.condition4OHT],
                   'total_dose': [100, 100, 100, 100, 100, 100, 200, 200, 200, 200,
                                  200, 200],
                   'num_injections': [2, 2, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2]})