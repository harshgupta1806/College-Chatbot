from imports import *

# --------------------------------------------------------------


def get_news():
    html = to_soup.get_html(news_url)
    soup = to_soup.get_soup(html)

    print("Fetching recent news...")
    headers = soup.findAll('header', attrs={"class": "entry-header"})
    recent_news = {}
    news = []

    for header in headers:
        n = {}
        a = header.findChild("h2").findChild("a")
        n['news'] = a.text
        n['link'] = a.get('href')
        news.append(n)

    print(f"Found {len(news)} recent news.")
    recent_news["recent-news"] = news
    return recent_news


def get_events():
    html = to_soup.get_html(events_url)
    soup = to_soup.get_soup(html)

    print("Fetching latest events...")
    print("Fetching recent news...")
    headers = soup.findAll('header', attrs={"class": "entry-header"})
    latest_event = {}
    events = []

    for header in headers:
        e = {}
        a = header.findChild("h2").findChild("a")
        e['event'] = a.text
        e['link'] = a.get('href')
        events.append(e)

    print(f"Found {len(events)} events.")
    latest_event["latest-events"] = events
    return latest_event


# --------------------------------------------------------------


def send_news():
    msg = ''
    recent_news = get_news()
    for news in recent_news['recent-news']:
        result1 = news['news']
        result2 = news['link']
        msg = msg + result1 + '\n' + result2 + '\n\n'
    return msg


def send_event():
    msg = ''
    recent_events = get_events()
    for news in recent_events['latest-events']:
        result1 = news['event']
        result2 = news['link']
        msg = msg + result1 + '\n' + result2 + '\n\n'
    return msg


# --------------------------------------------------------------

if __name__ == '__main__':
    # print(get_news())
    # print(get_events())
    send_event()

# --------------------------------------------------------------
