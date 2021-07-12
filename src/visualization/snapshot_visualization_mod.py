# -*- coding: utf-8 -*-
"""
Created on Wednesday 24 March 2021

Snapshot pilot visualization module.

To be used with the spreadsheet stored at \snapshot_pilot\SS_data_collector.xlsx
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
        self.groupbymouse = self.df.groupby("mouse")
        self._mousedf = self.groupbymouse.get_group(mouse)
        self._condition4OHT = self._mousedf["condition"].unique()[0]
        
    #Get the basic counts:
        self._green_cells = self._mousedf.sum()["green"]
        self._red_cells = self._mousedf.sum()["red"]
        self._double_cells = self._mousedf.sum()["double"]
        
        self._green_cort = self._mousedf.sum()["green_cortex"]
        self._red_cort = self._mousedf.sum()["red_cortex"]        
        self._double_cort = self._mousedf.sum()["double_cortex"]
        
        self._green_thal = self._mousedf.sum()["green_thal"]
        self._red_thal = self._mousedf.sum()["red_thal"]
        self._double_thal = self._mousedf.sum()["double_thal"]
        
        self._total_cells = self._red_cells + self._green_cells + self._double_cells
        self._green_std = np.std(self._mousedf["green_only_proportion"])
        self._red_std = np.std(self._mousedf["red_only_proportion"])      
        
        self._total_cort = self._red_cort + self._green_cort + self._double_cort
        self._total_thal = self._red_thal + self._green_thal + self._double_thal
        
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
    def green_std(self):
        return self._green_std
    
    @property
    def red_std(self):
        return self._red_std
    
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
    
    @property
    def green_prop_cort(self):
        return self._green_cort/self._total_cort
    
    @property
    def red_prop_cort(self):
        return self._red_cort/self._total_cort

    @property
    def green_prop_thal(self):
        return self._green_thal/self._total_thal
    
    @property
    def red_prop_thal(self):
        return self._red_thal/self._total_thal    
    
    
    @property
    def mouse_df(self):
        return self._mousedf
    
    
    def get_gfpboost_slices(self, gfpboost_amt):
        return self._mousedf.loc[self._mousedf['nanobooster'] == gfpboost_amt]
        

    def get_slide(self, slide):
        """Returns a dataframe including all slices from a given slide from the mouse"""
        return self._mousedf.loc[self._mousedf['slide'] == slide]
    
    def get_subset(self, col_title, group):
        """Returns a dataframe that only includes rows that have group as a value in col_title"""
        return self._mousedf.loc[self._mousedf[col_title] == group]
        
    
### Functions for doing things with multiple mice:

def concat_dfs(list_of_dfs):
    """Returns a dataframe containing all rows of the dataframes in the list. 
    Example: if list_of_dfs = [MouseA.mouse_df, MouseB.mouse_df], then this function will return one df with 
    all rows for these mice. Input dfs must have the same column names."""
    return pd.concat(list_of_dfs)

def get_counts_subset(subset_df):
        """Returns basic cell counts for a dataframe spliced from the mouse's dataframe
        Example: input the result of the get_gfpboost_slices function to get cell counts
        for just slices with the given gfp booster amount."""
        subset_green_cells = subset_df.sum()["green"]
        subset_red_cells = subset_df.sum()["red"]
        subset_double_cells = subset_df.sum()["double"]
        subset_total_cells = subset_red_cells + subset_green_cells + subset_double_cells
        #TODO make this return a clear text statement so user knows which number is which
        return subset_green_cells, subset_red_cells, subset_double_cells, subset_total_cells
