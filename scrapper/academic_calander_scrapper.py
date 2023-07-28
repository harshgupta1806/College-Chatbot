from imports import *


def get_academic_calander():
    html = to_soup.get_html(ac_url)
    soup = to_soup.get_soup(html)
    a_s = soup.find('div', attrs={"class": "content-area", "id": "primary"}).findChild('main').findChild(
        'article').findAll('a')

    academic_calander = {}
    details = []
    for a in a_s:
        detail = {}
        btn = a.findChild('button')
        span = a.findChild('span')

        if btn is not None:
            detail["detail"] = btn.text
        elif span is not None:
            detail["detail"] = span.text

        detail["link"] = a.get('href')
        details.append(detail)
    academic_calander["academic-calander"] = details

    print(f"Found {len(details)} links")
    return academic_calander


if __name__ == '__main__':
    print(get_academic_calander())
