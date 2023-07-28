from scrapper import scheme_scrapper
from scrapper.urls import scheme_links
from database import syllabus_db
import time


def store_syllabus_to_db(branch):
    # todo: store first syll in another table
    # todo: check if first syll = new syll; if yes send alert
    # todo: truncate table
    start = time.time()

    syllabus_obj = {
        'branch': '',
        'semester': '',
        'title': '',
        'link': ''
    }

    syllabus = scheme_scrapper.get_schemes(branch)
    for items in syllabus.items():
        syllabus_obj['branch'] = branch
        syllabus_obj['semester'] = '0'
        syllabus_obj['title'] = items[0]
        syllabus_obj['link'] = items[1]
        syllabus_db.save_syllabus_details_to_db(syllabus_obj)
    end = time.time()
    print("time elapsed: {:.2f}s".format(end-start))


store_syllabus_to_db('cse')
