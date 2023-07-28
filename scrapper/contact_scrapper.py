from imports import *

# in case urls.py not updated uncomment it
# contactus_url = 'https://ies.ipsacademy.org/#contact'



# --------------------------------------------------------------

def get_contact_info():
    html = to_soup.get_html(contactus_url)
    soup = to_soup.get_soup(html)

    contact_info = ""
    contacts = soup.find('section', attrs={"id": "contact"}).find('div', attrs={"class": "container"}).findChildren(
        'div', attrs={"class": "address-contact"})

    other_info = contacts[-1]
    contacts = contacts[:-1]

    for contact in contacts:
        contact_info += f"{contact.findChild('div').text} \n"

    contact_info += "\n"

    p_s = other_info.findChildren('p')
    for p in p_s:
        contact_info += f"{p.text} \n"

    return contact_info


# --------------------------------------------------------------

if __name__ == '__main__':
    print(get_contact_info())
    # get_contact_info()

# --------------------------------------------------------------
