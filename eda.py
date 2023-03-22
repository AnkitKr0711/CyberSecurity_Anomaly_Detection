import pandas as pd

def total_observation(df):
    return df.shape[0]

def total_feature(df):
    return df.shape[1]

def missing(df):
    return df.isnull().sum().sum()

def duplicate(df):
    return df.duplicated().sum()

def data_type(df):
    return df.dtypes.value_counts()

def features(series):
    if series.dtypes in ['int64', 'float']:
        unq_var = len(series.unique())
        miss = series.isnull().sum()
        mean = series.mean()
        median = series.median()
        min = series.min()
        max = series.max()
        frame = pd.DataFrame([unq_var, miss, mean, median,min, max],
                             index=['unique value', 'missing', 'mean', 'median', 'min', 'max'])
    else:
        unq_var = len(series.unique())
        miss = series.isnull().sum()
        mode = series.mode()
        frame = pd.DataFrame([unq_var, miss, mode], index=['unique value', 'missing', 'Most used'])
    return frame

