import numpy as np,pandas as pd,re
from pandas.api.types import  is_string_dtype,is_numeric_dtype
from sklearn.ensemble import forest

#Converting the date field to various fields <saledate >
def add_datepart(df, fldname, drop=True):
    fld = df[fldname]
    if not np.issubdtype(fld.dtype, np.datetime64):
        df[fldname] = fld = pd.to_datetime(fld, infer_datetime_format=True)
    targ_pre = re.sub('[Dd]ate$', '', fldname)
    for n in ('Year', 'Month', 'Week', 'Day', 'Dayofweek', 'Dayofyear',
            'Is_month_end', 'Is_month_start', 'Is_quarter_end', 'Is_quarter_start', 'Is_year_end', 'Is_year_start'):  
        df[targ_pre+n] = getattr(fld.dt,n.lower())
    df[targ_pre+'Elapsed'] = fld.astype(np.int64) // 10**9
    if drop: df.drop(fldname, axis=1, inplace=True)

#Converting categorical variables to numbers
def conv_to_cats(df):
    for n,c in df.items():
        if is_string_dtype(c): df[n] = c.astype('category').cat.as_ordered()

#Replace missing values
def fix_missing(df,col):
    if is_numeric_dtype(df[col]):
        df[col+'_na']= pd.isnull(df[col])
        df[col]= df[col].fillna(df[col].median())

#Replace Categorical variable with their codes
def numericalize(df,col):
    if not is_numeric_dtype(df[col]):
        df[col+'_num']= df[col].cat.codes+1

# Random sampling of rows for the random forest 
def set_rf_samples(n):
    """ Changes Scikit learn's random forests to give each tree a random sample of
    n random rows.
    """
    forest._generate_sample_indices = (lambda rs, n_samples:
        forest.check_random_state(rs).randint(0, n_samples, n))
    
def reset_rf_samples():
    """ Undoes the changes produced by set_rf_samples.
    """
    forest._generate_sample_indices = (lambda rs, n_samples:
        forest.check_random_state(rs).randint(0, n_samples, n_samples))