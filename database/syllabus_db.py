import database.database as db  # comment when calling from same file
# import database as db  # uncomment when calling from same file
import database.students_db as st_db  # comment when calling from same file
# import students_db as st_db  # uncomment when calling from same file


def truncate_syllabus():
    print("inside truncate_syllabus")
    query = f"TRUNCATE syllabus_schema.syllabus"
    # db.execute_update(query)
    db.execute_update(query)

def insert_into_syllabus(syllabus_obj):
    print("inside insert_into_syllabus")
    branch = syllabus_obj['branch']
    semester = syllabus_obj['semester']
    title = syllabus_obj['title']
    link = syllabus_obj['link']

    query = f"INSERT INTO syllabus_schema.syllabus(branch, semester, title, link) VALUES('{branch}', '{semester}', '{title}', '{link}')"
    db.execute_update(query)


def select_from_syllabus(branch):
    print("inside select_from_syllabus")

    query = f"SELECT title, link  FROM syllabus_schema.syllabus WHERE branch='{branch}'"
    result = db.execute_query(query)
    return result


# ------------------------------------------------------------------------------

def get_syllabus_by_branch(chat_id):
    print("inside get_syllabus_by_branch")
    branch = st_db.get_branch_of_student(chat_id).lower()
    print(f"Branch Retrieved: {branch}\n")

    if branch in ['cse', 'csit', 'cst', 'cse-iot', 'cse-ds']:
        branch = 'cse'

    result = select_from_syllabus(branch)
    return result


if __name__ == '__main__':
    syllabuses = get_syllabus_by_branch('1522823114')
    for syllabus in syllabuses:
        print(syllabus[0] + "\n" + syllabus[1] + '\n\n')
# ------------------------------------------------------------------------------
