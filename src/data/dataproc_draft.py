# -*- coding: utf-8 -*-
"""
Created on Wednesday 24 March 2021

Snapshot pilot data processing module.
To be used with the spreadsheet stored at I:\Danielle Paynter\InVivoTTTPilots\snapshot_4OHT_pilot\references\SS4OHT_slide_summary.xlsx
which contains: list of mice/slides/slices obtained through snapshot pilot experiment, raw cell counts by slice, basic histology info,
and the 4OHT dosage the mouse received.

This module is designed so that each mouse has its own Class object. 

@author: dpaynter
"""

import pandas as pd
import numpy as np

class snapshot_mouse(object):
    """Class that holds a single mouse from the snapshot pilot"""
    
    def __init__( self, mouse, datapath ) :
        
        self.mouse = mouse
        self.df = pd.read_excel(datapath)
        #TODO make all dashes NaN at import
        
        #Get mouse-specific info from spreadsheet:
        self.groupbymouse = self.df.groupby("Mouse")
        self._mousedf = self.groupbymouse.get_group(mouse)
        self._condition4OHT = self._mousedf["Condition"].unique()[0]
        
    #Get the basic counts:
        self._green_cells = self._mousedf.sum()["Green_only_Count"]
        self._red_cells = self._mousedf.sum()["Red_only_Count"]
        self._double_cells = self._mousedf.sum()["Double_labeled_Count"]
        self._total_cells = self._red_cells + self._green_cells + self._double_cells
        
    ## Properties:
    def __str__(self):
        """ Returns a printable string with summary output """
        return "Things are fine so far!"
    
    @property
    def condition4OHT(self):
        return self._condition4OHT
    
    @property
    def green_cells(self):
        return self._green_cells
    
    @property
    def red_cells(self):
        return self._red_cells
    
    @property
    def double_cells(self):
        return self._double_cells
    
    @property    
    def total_cells(self):
        return self._total_cells
    
    @property
    def green_only_prop(self):
        return self._green_cells/self._total_cells
    
    @property
    def red_only_prop(self):
        return self._red_cells/self._total_cells
    
    def get_gfpboost_slices(self, gfpboost_amt):
        return self._mousedf.loc[self._mousedf['GFP_booster'] == gfpboost_amt]
        
    def get_counts_subset(self, subset_df):
        """Returns basic cell counts for a dataframe spliced from the mouse's dataframe
        Example: input the result of the get_gfpboost_slices function to get cell counts
        for just slices with the given gfp booster amount."""
        subset_green_cells = subset_df.sum()["Green_only_Count"]
        subset_red_cells = subset_df.sum()["Red_only_Count"]
        subset_double_cells = subset_df.sum()["Double_labeled_Count"]
        subset_total_cells = subset_red_cells + subset_green_cells + subset_double_cells
        return subset_green_cells, subset_red_cells, subset_double_cells, subset_total_cells

        
        
        
        
        
        