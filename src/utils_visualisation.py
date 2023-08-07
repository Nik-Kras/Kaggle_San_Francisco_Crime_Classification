"""
This module will contain functions that will be used to visualize the data
"""
import pandas as pd

# Example of good function
def show_top_5_rows(df: pd.DataFrame) -> None:
    """
    Function that will show top 5 rows of the dataset
    :param df: pd.DataFrame
    :return: None
    """
    print(df.head(5))
    
    
def count_missing_values(df: pd.DataFrame):
    """
    Function that will count missing values in the dataset
    :param df: pd.DataFrame
    :return: ???
    """
    ### Write a function that takes a dataset and count how many None / Missing Values
    ### There are for each column separately
    ### For Example:
    ### Dataset: 
    #       [1,    0,    None]
    #       [2,    9,    0]
    #       [4,    0,    2]
    #       [None, 0,    2]
    #       [6,    4,    3]
    #       [1,    0,    None]
    ###     Column 1: 1
    ###     Column 2: 0
    ###     Column 3: 2


    # Do a doubke loop
    # Do a .isnull() check