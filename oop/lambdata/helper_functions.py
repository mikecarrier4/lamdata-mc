"""Helper Function"""
import pandas as pd
import numpy as np
from numpy import nan

def DataFrame (filename):
    df = pd.read_csv(filename)
    return df


class DataFrameFunctions():

    def __init__(self, df):
        self.df = df

    def head(self):
        return self.df.head()
    
    def null_count(self):
        return self.df.isna().sum().sum()

    def randomizer(self, seed):
        self.df.sample(frac = 1, random_state = seed).reset_index(drop = True)
        return self.df

""" Converts Array or List to Pandas Series"""    
class PandaSeriesFunction():
    
    def __init__(self, array):
        self.array = array

    def array_to_series(self):
        t = pd.Series(self.array)
        return t

    
    
