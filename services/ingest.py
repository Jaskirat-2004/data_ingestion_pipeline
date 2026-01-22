import pandas as pd

expected_cols=(
    'date',
    'emp_id',
    'name',
    'process_name',
    'location',
    'shift_name',
    'shift_type',
    'tl_name',
    'attendance',
    'in_time',
    'ad_non_ad'
)

def read_clean(file_obj,filename:str):

    if filename.endswith((".xlsx",".csv")):

        if filename.endswith(".xlsx"):
            df = pd.read_excel(file_obj)
        else:
            df = pd.read_csv(file_obj)
            
        df = df.loc[:,~df.columns.str.contains('^Unnamed')]
        df = df.where(pd.notna(df),None)

        if df.empty:
            return None,"FILE EMPTY"
    
        if df.shape[1] < len(expected_cols):
            return None,"COLUMNS ARE LESS THAN REQUIRED"
        
        if df.shape[1] > len(expected_cols):
            return None,"COLUMNS ARE MORE THAN REQUIRED"


        return df,None
    
    else:
        return None,"ONLY CSV AND XLSX ALLOWED"