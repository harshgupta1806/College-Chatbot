import database.database as db  # comment when calling from same file
# import database as db  # uncomment when calling from same file


def insert_into_faculty(faculty_obj):
    print("inside save_faculty_details")
    chat_id = faculty_obj['chat_id']
    department = faculty_obj['department']

    query = f"INSERT INTO user_details_schema.faculty(chat_id, department) VALUES('{chat_id}', '{department}')"
    db.execute_update(query)


def update_faculty_set_department(faculty_obj):
    print("inside update_faculty_department")
    chat_id = faculty_obj['chat_id']
    department = faculty_obj['department']
    query = f"UPDATE user_details_schema.faculty SET department = '{department}' WHERE chat_id = '{chat_id}'"
    db.execute_update(query)


def delete_faculty_details(chat_id):
    print("inside delete_faculty_details")
    query = f"DELETE FROM user_details_schema.faculty WHERE chat_id = '{chat_id}'"
    db.execute_update(query)


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    faculty_object = {
        'chat_id': '1128669512',
        'department': 'cse'
    }
    # insert_into_faculty(faculty_object)
    faculty_object = {
        'chat_id': '1128669512',
        'department': 'me'
    }
    # update_faculty_set_department(faculty_object)
    # delete_faculty_details('1128669512')
# ------------------------------------------------------------------------------
