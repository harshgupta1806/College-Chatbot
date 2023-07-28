import database.database as db  # comment when calling from same file
# import database as db  # uncomment when calling from same file


def insert_into_student(student_obj):
    print("inside insert_into_student")

    chat_id = student_obj['chat_id']
    branch = student_obj['branch']
    year = student_obj['year']

    query = f"INSERT INTO students(chat_id, branch,year) VALUES('{chat_id}', '{branch}','{year}')"
    db.execute_update(query)


def insert_branch_into_student(student_obj):
    print("inside update_student_set_branch")

    chat_id = student_obj['chat_id']
    branch = student_obj['branch']
    query = f"INSERT into user_details_schema.students(chat_id, branch) VALUES('{chat_id}', '{branch}')"
    db.execute_update(query)


def update_student_set_year(student_obj):
    print("inside update_student_set_branch")

    chat_id = student_obj['chat_id']
    year = student_obj['year']
    query = f"UPDATE user_details_schema.students SET year = '{year}' WHERE chat_id = '{chat_id}'"
    db.execute_update(query)


def delete_student_details(chat_id):
    print("inside delete_faculty_details")
    query = f"DELETE FROM user_details_schema.students WHERE chat_id = '{chat_id}'"
    db.execute_update(query)


def get_branch_of_student(chat_id):
    print("inside get_branch_of_student")
    query = f"SELECT branch FROM user_details_schema.students WHERE chat_id = '{chat_id}'"
    result = db.execute_query(query)
    if result is None or len(result) == 0:
        return None
    return result[0][0]
