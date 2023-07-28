from scrapper import notice_scrapper
from scrapper import department_notice_scrapper
from scrapper.urls import department_notice_url
from database import notice_board_db
import time


def store_notice_to_db(branch="college"):
    # todo: store first notice in another table
    # todo: check if first notice = new notice; if yes send alert
    # todo: truncate table
    start = time.time()
    if branch == 'college':
        notices = notice_scrapper.get_formatted_notice()
    else:
        notices = department_notice_scrapper.get_department_notice(branch)
    for notice in notices:
        notice_board_db.insert_into_notice_board(notice_title=notice['Notice'], notice_link=notice['Link'], notice_type=branch)
    end = time.time()
    print("time elapsed: {:.2f}s".format(end-start))


def store_department_notice_to_db():
    for branch in department_notice_url.keys():
        store_notice_to_db(branch)


store_notice_to_db()
store_department_notice_to_db()
