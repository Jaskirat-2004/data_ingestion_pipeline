import psycopg2

def get_conn():
    conn = psycopg2.connect(
        host="localhost",
        database="pg_practice",
        user="postgres",
        password="jaskirat",
        port=5432
    )
    print(" <<< Connected to DB >>>")
    return conn
