import database.database as db  # comment when calling from same file
# import database as db  # uncomment when calling from same file
import database.students_db as st_db  # comment when calling from same file
# import students_db as st_db  # uncomment when calling from same file


def truncate_notice_board():
    print("inside truncate_notice_board")
    query = f"TRUNCATE notice_board_schema.notice_board;"
    db.execute_update(query)


def insert_into_notice_board(notice_title: str, notice_link: str, notice_type: str = 'college'):
    print("inside insert_into_notice_board")
    query = f"INSERT INTO notice_board_schema.notice_board(notice_title, notice_link , notice_type) VALUES('{notice_title}', '{notice_link}', '{notice_type}')"
    db.execute_update(query)


def select_from_notice_board(branch):
    print("inside select_from_notice_board")

    query = f"SELECT notice_title, notice_link  FROM notice_board_schema.notice_board WHERE notice_type='{branch}' order by scrapped_on"
    result = db.execute_query(query)
    return result


def get_notice_by_branch(chat_id):
    print("inside get_notice_by_branch")
    branch = st_db.get_branch_of_student(chat_id)
    branch = str(branch)
    branch.lower()
    print(f"Branch Retrieved: {branch}\n")

    if branch in ['cse', 'csit', 'cst', 'cse-iot', 'cse-ds']:
        branch = 'cse'

    result = select_from_notice_board(branch)
    return result

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    print(select_from_notice_board('cse'))
# ------------------------------------------------------------------------------
