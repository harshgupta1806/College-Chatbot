from scrapper import scheme_scrapper
from scrapper.urls import scheme_links
from database import syllabus_db
import time


def store_syllabus_to_db(branch):
    # todo: store first notice in another table
    # todo: check if first notice = new notice; if yes send alert
    start = time.time()

    syllabuses = scheme_scrapper.get_schemes(branch)
    i = 3
    for syllabus in syllabuses.items():
        syllabus_obj = {'branch': branch, 'semester': i, 'title': syllabus[0], 'link': syllabus[1] }
        syllabus_db.insert_into_syllabus(syllabus_obj=syllabus_obj)
        i += 1
    end = time.time()
    print("time elapsed: {:.2f}s".format(end-start))


def store_all_syllabus_to_db():
    start = time.time()
    syllabus_db.truncate_syllabus()
    for branch in scheme_links.keys():
        store_syllabus_to_db(branch)
    end = time.time()
    print("Total time elapsed: {:.2f}s".format(end-start))


if __name__ == '__main__':
    store_all_syllabus_to_db()
