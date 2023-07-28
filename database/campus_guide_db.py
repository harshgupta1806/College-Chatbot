import database.database as db

def insert_into_campus_guide(cg_obj):
    print("inside save_campus_guide_details")

    title = cg_obj['title']
    first_name = cg_obj['first_name']
    last_name = cg_obj['last_name']
    designation = cg_obj['designation']
    department = cg_obj['department']
    contact = cg_obj['contact']
    email = cg_obj['email']
    cabin = cg_obj['cabin']

    query = f"INSERT INTO campus_guide_schema.faculty_details(title, first_name, last_name, designation, department, contact, email, cabin) VALUES ('{title}', '{first_name}', '{last_name}', '{designation}', '{department}', '{contact}', '{email}', '{cabin}')"
    db.execute_update(query)


def select_from_campus_guide(first_name, last_name=None, department=None):
    print("inside select_from_campus_guide")
    if last_name is None:
        query = f"SELECT * FROM campus_guide_schema.faculty_details WHERE first_name = '{first_name}'"
    else:
        query = f"SELECT * FROM campus_guide_schema.faculty_details WHERE first_name = '{first_name}' and (last_name = '{last_name}' or department = '{last_name}') "

    if last_name is not None and department is not None:
        query = f"SELECT * FROM campus_guide_schema.faculty_details WHERE first_name = '{first_name}' and last_name = '{last_name}' and department = '{department}' "

    result = db.execute_query(query)
    return result


if __name__ == '__main__':
    # cg = {
    # 'title': 'Ms.'
    #     'first_name': 'shefali', 'last_name': 'aggarwal', 'designation': 'assistant professor', 'department': 'cse',
    #     'contact': '999999999', 'email': 'shefali_aggrwal@ipsacademy.org', 'cabin': '108-B'
    # }
    #
    # insert_into_campus_guide(cg)
    select_from_campus_guide_('')
