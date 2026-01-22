import psycopg2
import pandas as pd
import time
from io import StringIO

start_time  =  time.time()

conn = psycopg2.connect(
    host="localhost",
    database="pg_practice",
    user="postgres",
    password="jaskirat",
    port=5432
)

cur = conn.cursor()
print("Connected to DB")

cur.execute("""
            CREATE TABLE IF NOT EXISTS shift_adherence (
            id SERIAL,
            date DATE,
            emp_id TEXT,
            name TEXT,
            process_name TEXT,
            location TEXT, 
            shift_name TEXT,
            shift_type TEXT,
            tl_name TEXT,
            attendance TEXT,
            in_time TIME,
            ad_non_ad TEXT,
            PRIMARY KEY(date,emp_id)
            )""")

cur.execute("TRUNCATE TABLE shift_adherence RESTART IDENTITY")

df = pd.read_csv(r"C:\Users\8242K\Desktop\WFM\Pan India\Pan India Shift Adherence\FINAL_COLLATED.csv")
df = df.loc[:,~df.columns.str.contains('^Unnamed')]
df = df.where(pd.notna(df),None)

buffer = StringIO()
df.to_csv(buffer,index=False,header=False,na_rep='\\N')
buffer.seek(0)
cols=(
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
cur.copy_from(buffer,'shift_adherence',sep=',',columns=cols)

conn.commit()

total_time =  time.time()
print(f"Time taken : {(total_time-start_time):.2f}s")