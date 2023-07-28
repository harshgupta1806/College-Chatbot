import re

start = re.compile("/start|start")

unsubscribe = ("unsubscribe|stop")

menu = re.compile("/menu|menu|service")

greeting = re.compile("hi|hii|hello|hey|namaste|what's up|hy|hye")

# -------------------------------------------------------

contact = re.compile("contact|info|information|number|phone|mobile|no\.")

academic_calender = re.compile("calender|calander|calandar|calandr|calendar")

admission = re.compile("addmission|admition|addmision|admision|admission")

notices = re.compile("notice|notices|notice board|notice bord")

syllabus = re.compile("syllabus|scheme|sylabus|sillabus|syllbus|sceme")

cse = re.compile("cse|csit|cse_csit|iot|ds|cse-iot|cse-ds|data science|computer science|internet of things")

mechanical = re.compile("mechanical|mechecnical|machanial|mechenical")

electrical = re.compile("electrial|electric")

civil = re.compile("civil|ce")

chemical = re.compile("chemical|cm")

ft = re.compile("ft|fire|firetech")

electronics = re.compile("electronics|electronic|ec")

news = re.compile("news")

event = re.compile("event|function")

# -------------------------------------------------------

campusguide = re.compile("cg")

notes = re.compile("notes")

faq = re.compile("faq|help|question|query|queries|frequently aske?")
