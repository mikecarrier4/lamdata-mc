"""Helper Function"""
import pandas as pd
import numpy as np
from numpy import nan

data = [[nan, 4, 3], [9, nan, nan], [10, 2, 2]]



df = pd.DataFrame(data, index = [0,1,2], columns = ['column 0', 'column 1', 'column 2'])


"""Counts Null in Pandas Dataframes"""
def null_count(DataFrame):
    x = DataFrame.isna().value_counts().sum()
    print(x)
    return x

"""Randomizer of DF"""
def randomizer(df, seed):
    df = df.sample(frac =1 , random_state = seed).reset_index(drop = True)
    print(df)



