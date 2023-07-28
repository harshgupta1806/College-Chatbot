
greeting_replies = ["Hi!!!!", "Hello :)", "Namastey", "Hey", "How May I Help You"]

API_KEY = '5001784422:AAEiOqclep4fPcGBryVcpM7muzQ_raJ_oKk'

dept_links = {
    "civil": "https://ies.ipsacademy.org/departments/civil-engg/",
    "cse_csit": "https://ies.ipsacademy.org/departments/computer-science-engg/",
    "chemical": "https://ies.ipsacademy.org/departments/chemical-engg/b-tech-chemical-engineering-",
    "electrical": "https://ies.ipsacademy.org/departments/elect-elex-engg/",
    "electronics": "https://ies.ipsacademy.org/departments/electronics-communication/",
    "ft": "https://ies.ipsacademy.org/departments/fire-tech-safety-engg/",
    "mechanical": "https://ies.ipsacademy.org/departments/mechanical-engg/"
}

dept_name = ['civil', 'cse_csit', 'chemical', 'electrical', 'ft', 'mechanical', 'electronics']

branch = ['set_branch:CSE', 'set_branch:CSIT', 'set_branch:CSE-IOT', 'set_branch:CSE-DS', 'set_branch:CIVIL', 'set_branch:CHEMICAL', 'set_branch:ELECTRICAL', 'set_branch:EC', 'set_branch:FT', 'set_branch:MECHANICAL']
syllabus = ['get_scheme:CSE', 'get_scheme:CIVIL', 'get_scheme:CHEMICAL', 'get_scheme:ELECTRICAL', 'get_scheme:EC', 'get_scheme:FT', 'get_scheme:MECHANICAL', 'get_scheme:First Year']
other_syllabus = ['get_other_scheme:CSE', 'get_other_scheme:CIVIL', 'get_other_scheme:CHEMICAL', 'get_other_scheme:ELECTRICAL', 'get_other_scheme:EC', 'get_other_scheme:FT', 'get_other_scheme:MECHANICAL', 'get_other_scheme:First Year']

get_notice = ['get_notice:COLLEGE NOTICE BOARD', 'get_notice:DEPARTMENT NOTICE BOARD', 'get_notice:OTHER DEPARTMENT NOTICE']
other_notice = ['get_other_notice:CSE', 'get_other_notice:CIVIL', 'get_other_notice:CHEMICAL', 'get_other_notice:ELECTRICAL', 'get_other_notice:EC', 'get_other_notice:FT', 'get_other_notice:MECHANICAL']
year = ['I', 'II', 'III', 'IV']



intro = ''' Hello, I am IES-Chatbot.
          Ask for 'menu' for more details....
          '''

# menu = ['menu:Syllabus & Scheme', 'menu:Notice', 'menu:Addmission Enquiry', 'menu:College Information', 'menu:Campus Guide',
#         'menu:Academic Calender', 'menu:News','menu:Events', 'menu:FAQ', 'menu:RGPV NOTES']


menu = ['menu:Syllabus', 'menu:Notice-Board', 'menu:Admission Enquiry', 'menu:College Information', 'menu:Campus Guide',
        'menu:Academic Calender', 'menu:Latest News','menu:Events', 'menu:FAQ', 'menu:RGPV-NOTES']


campus_guide_intro = """
please specify the name of faculty you are looking for

please see the below input format
cg <first_name> [<last_name> :optional] [<department> :optional]
example:

cg jaydeep
cg jaydeep sahu
cg jaydeep cse
cg jaydeep sahu cse

Please be specific while mentioning department.
available choices:- 
cse, mechanical, electrical, electronics, ft, cm (for chemical) etc.
"""

rgpv_notes_intro = """
please specify the subject you are looking for

please see the below input format
notes <subject_name>
notes <subject_acronym>
example:

notes operating system
notes os

Please be specific while mentioning subject. 
Make sure that there is no spelling mistake. We understand that 'to err is human' 
our team is continuosly working for improvement. Thanks for your time.
"""