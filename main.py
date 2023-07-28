import re
import command
import connection_bot as cb
import constants.constant
import database.notice_board_db
from constants import search_keyword
from scrapper import urls
from scrapper import admission_scrapper
from scrapper import contact_scrapper
from scrapper import news_event_scrapper as nes
from database import database
from database import users_db
from database import students_db
from database import faculty_db
from database import users_db
from database import notice_board_db
from database import syllabus_db
from database import campus_guide_db
from database import rgpv_notes_db

from nltk_processing import nltk_file

bot = cb.get_bot()

_id = None


@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global _id
    # getting pressed data from button
    data = call.data.split(':')
    reason = data[0]
    data = data[1]

    # getting user chat id
    user_chat_id = call.message.json['chat']['id']

    # set branch in database
    if reason == 'set_branch':
        print(call)
        bot_message_id = call.message.json['message_id']
        # print(bot_message_id)
        # print(user_chat_id)
        bot.delete_message(user_chat_id, bot_message_id)
        print("Message Deleted")
        bot.send_message(user_chat_id, 'Your Branch has been Updated Successfully. This will help us in giving you '
                                       'more personalized content in future.')
        command.intro(user_chat_id)
        student_obj = {
            'chat_id': user_chat_id,
            'branch': data,
            'year': None
        }
        students_db.insert_branch_into_student(student_obj)

    # handles the syllabus & scheme
    elif reason == 'get_branch_syllabus' or reason == 'get_other_scheme':
        if reason == 'get_branch_syllabus':
            bot_message_id = call.message.json['message_id']
            bot.delete_message(user_chat_id, bot_message_id)
        if data == 'First Year' or data == 'Your Branch':
            if data == 'First Year':
                bot.send_message(user_chat_id, "Fetching Syllabus of First Year")
                results = syllabus_db.select_from_syllabus('general')
            elif data == 'Your Branch':
                bot.send_message(user_chat_id, "Fetching Syllabus of your branch")
                results = syllabus_db.get_syllabus_by_branch(user_chat_id)
            if results is None:
                bot.send_message(user_chat_id,
                                 "I am afraid something is wrong at my end :( \n I am sorry for this trouble.. I will get back to you as soon as possible.")
            else:
                for result in results:
                    bot.send_message(user_chat_id, result[0] + '\n' + result[1])
        elif data == 'Other':
            print('If other IS TAPPED .... ')
            command.scheme_keyboard(user_chat_id)
        elif reason == 'get_other_scheme':
            branch = data.lower()
            print('get_other_scheme - ', branch)
            bot.send_message(user_chat_id, f"Fetching Syllabus of {branch}")
            results = syllabus_db.select_from_syllabus(branch)
            bot.send_message(user_chat_id, f"Sending syllabus of {branch}")

    # notice
    elif reason == 'get_notice' or reason == 'get_other_notice':
        if data == 'DEPARTMENT NOTICE BOARD':
            bot.send_message(user_chat_id, "Fetching Department-Notice-Board...")
            dept_notices = notice_board_db.get_notice_by_branch(user_chat_id)
            if dept_notices is None:
                bot.send_message(user_chat_id,
                                 "I am afraid something is wrong at my end :( \n I am sorry for this trouble.. I will get back to you as soon as possible.")
            else:
                for dept_notice in dept_notices:
                    bot.send_message(user_chat_id, dept_notice[0] + '\n' + dept_notice[1])
        elif data == 'COLLEGE NOTICE BOARD' or reason == 'get_other_notice':
            notices = []
            if data == 'COLLEGE NOTICE BOARD':
                bot.send_message(user_chat_id, "Fetching College-Notice-Board..")
                notices = notice_board_db.select_from_notice_board('college')
            else:
                branch = data.lower()
                print('In other was pressed for - ', branch)
                bot.send_message(user_chat_id, f"Fetching Department-Notice-Board for {branch}..")
                notices = notice_board_db.select_from_notice_board(branch)
            if notices is None or len(notices) == 0:
                bot.send_message(user_chat_id,
                                 "I am afraid something is wrong at my end :( \n I am sorry for this trouble.. I will get back to you as soon as possible.")
            else:
                for notice in notices:
                    bot.send_message(user_chat_id, notice[0] + '\n' + notice[1])

        elif data == 'OTHER DEPARTMENT NOTICE':
            print('If other IS pressed .... ')
            command.other_notice_keyboard(user_chat_id)
        # for notice in notices:
        #     bot.send_message(user_chat_id, notice[0] + '\n' + notice[1])

        # menu
    elif reason == 'menu':
        bot.send_message(user_chat_id, "Please wait.. Let me go and get menu for you")

        if data == 'Syllabus':
            print('printing Syllabus & Scheme from menu')
            command.scheme(user_chat_id)
        elif data == 'Notice-Board':
            command.notice_keyboard(user_chat_id)
        elif data == 'Addmission Enquiry':
            bot.send_message(user_chat_id, admission_scrapper.get_admission_info())
        elif data == 'College Information':
            bot.send_message(user_chat_id, 'Fetching ....')
            bot.send_message(user_chat_id, contact_scrapper.get_contact_info())

        # CAMPUS GUIDE
        elif data == 'Campus Guide':
            bot.send_message(user_chat_id, text=constants.constant.campus_guide_intro)


        elif data == 'Academic Calender':
            bot.send_message(user_chat_id, "Fetching link for Academic Calender ")
            bot.send_message(user_chat_id, "Link :- " + urls.ac_url)
        elif data == 'News':
            bot.send_message(user_chat_id, nes.send_news())
        elif data == 'Events':
            bot.send_message(user_chat_id, nes.send_event())
        elif data == 'FAQ':
            bot.send_message(user_chat_id,
                             text="This feature is under development. It will be added in future releases.")
        elif data == 'RGPV-NOTES':
            bot.send_message(user_chat_id,
                             text=constants.constant.rgpv_notes_intro)

    else:
        pass


@bot.message_handler(content_types=['audio', 'photo', 'voice', 'video', 'document', 'location', 'contact', 'sticker'])
def reject(message):
    bot.send_message(message.chat.id, 'Sorry 😔😔, I can accept input in TEXT format only!!')


@bot.message_handler(content_types='text')
def main(message):
    print(message)
    count = 0
    msg = nltk_file.pass_message(message.text)
    user_chat_id = message.chat.id

    if re.search(search_keyword.greeting, msg) is not None:
        # greeting for user
        bot_message_id = bot.send_message(user_chat_id, command.greet() + ", " + message.from_user.first_name)
        count = 1

    if re.search(search_keyword.start, msg) is not None:
        # user presssed start
        print(msg)
        valid_user = users_db.validate_user(user_chat_id)
        if valid_user is True:
            bot.send_message(user_chat_id, 'You are already subscribed with us!! Press stop to unsubscibe')
        else:
            id = bot.send_message(user_chat_id,
                                  "Welcome!! Please fill the details to get subscribed with us.\nIt will take only few minutes!!")
            # print("Hii", bot_message_id)

            user_obj = {
                'chat_id': user_chat_id,
                'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name,
            }
            users_db.insert_into_users(user_obj)
            command.start(message)  # display inline button for branch

        count = 1
    if re.search(search_keyword.unsubscribe, msg) is not None:
        # user pressed stop
        bot.send_message(user_chat_id, 'Okay!! Now you will not recieve any notification from us')
        bot.send_message(user_chat_id, "If you want to subscribe again, send me a \'start\' message")
        users_db.delete_users_details(user_chat_id)
        count = 1
    if re.search(search_keyword.contact, msg) is not None:
        print("working")
        bot.send_message(user_chat_id, 'Fetching ....')
        bot.send_message(user_chat_id, contact_scrapper.get_contact_info())
    elif re.search(search_keyword.academic_calender, msg) is not None:
        print('working')
        bot.send_message(user_chat_id, "Fetching link for Academic Calender ")
        bot.send_message(user_chat_id, "Link :- " + urls.ac_url)
    elif re.search(search_keyword.admission, msg) is not None:
        print('working')
        bot.send_message(user_chat_id, admission_scrapper.get_admission_info())
    elif re.search(search_keyword.notices, msg) is not None:
        print('working')
        command.notice_keyboard(user_chat_id)
    elif re.search(search_keyword.syllabus, msg) is not None:
        print('working')
        command.scheme(user_chat_id)

    elif re.search(search_keyword.news, msg):
        bot.send_message(user_chat_id, nes.send_news())
    elif re.search(search_keyword.event, msg):
        bot.send_message(user_chat_id, nes.send_event())
    elif re.search(search_keyword.menu, msg) is not None:
        bot.send_message(user_chat_id, command.menu_keyboard(message))


    elif re.search(search_keyword.campusguide, msg) is not None:
        print("cg::")
        print("msg1 : " + msg)
        msg = msg.split('cg')
        args = msg[1].strip().split()
        args_len = len(args)

        if args_len not in [1, 2, 3]:
            bot.send_message(user_chat_id,
                             'It seems that given input is not in proper format.\n'
                             'Please click \'Campus Guide\' in menu for more instructions')
        else:
            bot.send_message(user_chat_id, "Ok please give me few seconds! let me go and get the details for you.")

            if args_len == 1:
                results = campus_guide_db.select_from_campus_guide(args[0], None, None)
            elif args_len == 2:
                results = campus_guide_db.select_from_campus_guide(args[0], args[1], None)
            elif args_len == 3:
                results = campus_guide_db.select_from_campus_guide(args[0], args[1], args[2])

            bot.send_message(user_chat_id, f"I have found {len(results)} matching results.")
            if results is not None:
                for result in results:
                    print(result)
                    output_template = f"""
    {result[0].title()} {result[1].title()} {result[2].title()}
    {result[4].title()}
    DEPARTMENT OF {result[3].upper()}
    CONTACT NUMBER: {result[5].title()}
    EMAIL ID: {result[6]}
    CABIN DETAILS: {result[7].lower()} 
                    """
                    bot.send_message(user_chat_id, output_template)

            bot.send_message(user_chat_id, "Thanks for your patience.")

    elif re.search(search_keyword.notes, msg) is not None:
        print("msg1 : " + msg)
        msg = msg.split('notes')
        args = msg[1].strip()
        #
        # bot.send_message(user_chat_id,
        #                  'It seems that given input is not in proper format.\n'
        #                  'Please click \'RGPV-Notes\' in menu for more instructions')
        bot.send_message(user_chat_id, "Ok please give me few seconds! let me go and get the details for you.")

        results = rgpv_notes_db.select_from_rgpv_notes(args)

        bot.send_message(user_chat_id, f"I have found {len(results)} matching results.")
        if results is not None:
            for result in results:
                print(result)
                output_template = f"""
    {result[0].title()}
    UNIT:  {result[1]}
    {result[2]} 
                        """
                bot.send_message(user_chat_id, output_template)
        bot.send_message(user_chat_id, "Thanks for your patience.")

    elif re.search(search_keyword.faq, msg) is not None:
        print("faq::")
        bot.send_message(user_chat_id, "This feature is under development. It will be added in future releases.")
    elif count == 1:
        pass
    else:
        bot.send_message(user_chat_id,
                         'Sorry!! I didnt get you :(\nAre you sure there is no spelling mistake? Could you please try again with different query?')
