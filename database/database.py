import database.connection_factory as cf  # comment when calling from same file
# import connection_factory as cf  # uncomment when calling from same file


def execute_update(query: str):
    """
    performs DML
    :param query: query to be executed
    """
    print(f"execute_update: {query}")
    cf.connect_to_db()
    if cf.is_connected_to_db():
        try:
            cf.cur.execute(query)
            print("Query executed successfully")
            cf.close_connection_with_db()
        except Exception as e:
            print("Failure")
            print(e)


def execute_query(query: str):
    """
    performs DQL
    :param query: query to be executed
    :return: list containing result rows
    """
    print(f"execute_query: {query}")
    cf.connect_to_db()
    if cf.is_connected_to_db():
        try:
            cf.cur.execute(query)
            result = cf.cur.fetchall()
            print(f"Query executed successfully. Returning {len(result)} rows.")
            cf.close_connection_with_db()
            return result
        except Exception as e:
            print("Failure")
            print(e)
            return None
