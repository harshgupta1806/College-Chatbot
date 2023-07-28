import psycopg2

conn = None  # connection object
cur = None  # cursor object


def connect_to_db():
    """
    connects to database
    """
    global conn, cur
    try:
        host = 'db.vpokgeykpgninfmritlv.supabase.co'
        user = 'postgres'
        pwd = 'harshgupta1806'
        dbname = 'postgres'

        conn = psycopg2.connect(host=host, user=user, password=pwd, database=dbname)
        print("Connected to database")
        cur = conn.cursor()

    except Exception as e:
        print(f"Could not connect to db : {e}")


def is_connected_to_db():
    """
    checks whether database is connected or not
    :return: True if connected else False
    """
    if conn and cur:
        return True
    return False


def close_connection_with_db():
    """
    commits changes to database
    closes connection with database
    """
    if is_connected_to_db():
        cur.close()
        conn.commit()
        print("Changes committed")

        conn.close()
        print("Connection closed")
