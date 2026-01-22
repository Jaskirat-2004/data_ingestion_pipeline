from db.connection import get_conn
from io import StringIO

def push_to_db(df):
        
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE shift_adherence RESTART IDENTITY")

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
    cur.close()
    conn.close()

    print("<"*5,"DATA PUSHED",">"*5)

