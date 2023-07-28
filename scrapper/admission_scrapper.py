from imports import *
# --------------------------------------------------------------

def get_admission_info():
    admission_info = "ADMISSION PROCEDURE\n\n"

    html = to_soup.get_html(admission_proc_url)
    soup = to_soup.get_soup(html)

    p_s = soup.find('div', attrs={"id": "primary"}).findChildren('p')
    for p in p_s:
        span = p.findChild('span')
        if span is not None:
            admission_info += f"{span.text}\n"
        else:
            admission_info += f"{p.text}\n"

    admission_rules = f"\n\nTo read more about admission rules please download following file.\n {admission_rules_link}"

    admission_info += admission_rules

    return admission_info


# --------------------------------------------------------------

if __name__ == '__main__':
    print(get_admission_info())
# --------------------------------------------------------------
