from imports import *


# --------------------------------------------------------------


# get unit
def get_units(soup):
    div = soup.findChildren('div', attrs={"class": "content section", "id": "content"})[0]
    units = div.find_all('ul', class_='text-left')[1].find_all('span', class_='Tooltip')

    # print(f"Fetched {len(units)} Units")
    print(f"Returning {len(units)} Units")
    return units


# get link from units
def get_link_from_units(units):
    links = []
    for unit in units:
        link = unit.find('a')
        links.append(link)
    return links


# merge unit link
def merge_units(links):
    units_link = []
    for link in links:
        data = {
            "unit": link.get('href')
        }
        if 'download' in data['unit']:
            units_link.append(data)
    return units_link


# --------------------------------------------------------------


# get rgpv notes:
def get_rgpv_notes(branch: str):
    # print("inside get_rgpv_notes")
    start_time = time.time()

    url = rgpv_notes_url[branch]

    html = to_soup.get_html(url)
    soup = to_soup.get_soup(html)

    units = get_units(soup)
    links = get_link_from_units(units)
    merge_unit = merge_units(links)

    end_time = time.time()
    print("Time Elapsed: {:.3f}s".format(end_time - start_time))
    return merge_unit


# --------------------------------------------------------------


if __name__ == '__main__':
    colect_unit = get_rgpv_notes("dsa")
    for collect in colect_unit:
        print(collect)

# --------------------------------------------------------------
