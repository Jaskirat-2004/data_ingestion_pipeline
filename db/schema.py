from db.connection import get_conn

def create_table():
    conn = get_conn()
    cur = conn.cursor()
    
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
    
    conn.commit()
    cur.close()
    conn.close()
