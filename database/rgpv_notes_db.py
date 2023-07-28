import database.database as db


def select_from_rgpv_notes(subject):
    print("inside select_from_rgpv_notes")
    subject = subject.strip()
    if subject is None or len(subject) == 0:
        return []
    query = f"SELECT  subject, unit_no, url FROM rgpv_notes_schema.rgpv_notes WHERE subject like '{subject}%' or abbr = '{subject}'"

    result = db.execute_query(query)
    return result


