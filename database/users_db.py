import database.database as db  # comment when calling from same file
# import database as db  # uncomment when calling from same file


def insert_into_users(user_obj):
    print("inside insert_into_users")
    # chat_id = message.chat.id
    # first_name = message.from_user.first_name
    # last_name = message.from_user.last_name
    chat_id = user_obj['chat_id']
    first_name = user_obj['first_name']
    last_name = user_obj['last_name']

    query = f"INSERT INTO user_details_schema.users(chat_id, first_name, last_name) VALUES('{chat_id}', '{first_name}', '{last_name}')"
    db.execute_update(query)


def update_users_details(user_obj):
    print("inside update_users_details")
    chat_id = user_obj['chat_id']
    first_name = user_obj['first_name']
    last_name = user_obj['last_name']

    query = f"UPDATE user_details_schema.users SET first_name = '{first_name}', last_name = '{last_name}' WHERE chat_id = '{chat_id}'"
    db.execute_update(query)


def delete_users_details(chat_id):
    print("inside delete_users_details")
    query = f"delete from user_details_schema.users where chat_id = '{chat_id}'"
    db.execute_update(query)

# ------------------------------------------------------------------------------


def validate_user(chat_id):
    print("inside validate_user")

    query = f"select * from user_details_schema.users where chat_id = '{chat_id}'"
    result = db.execute_query(query)
    if result is not None and len(result) > 0:
        return True
    return False


def get_chat_ids_of_all_users():
    print("inside get_chatid_of_all_users")
    query = f"select chat_id from user_details_schema.users"
    result = db.execute_query(query)
    return result

# ------------------------------------------------------------------------------
