from bs4 import BeautifulSoup
import requests
from requests import exceptions  
url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html#reporting-cases'

def get_state():
    
    params =None
    is_not_timeout, soup = get_soup(url, params)
    print(soup)
    # if is_not_timeout:
    #     is_not_blank, blank_result = no_trending(soup)
    #     if is_not_blank:
    #         developer_avatars = []
    #         for item in soup.find_all('img', attrs={'class': 'rounded-1'}):
    #             developer_avatars.append(item.attrs['src'].strip())
    #         user = []
    #         user_link = []
    #         full_name = []
    #         for item in soup.find_all('h1', attrs={'class': 'h3 lh-condensed'}):
    #             temp = item.a.attrs['href'].strip()
    #             user.append(temp[1:])
    #             user_link.append(GITHUB_URL + temp)
    #             full_n = ''#item.a.span
    #             if full_n is not None:
    #                 full_name.append(full_n.get_text().strip())
    #             else:
    #                 full_name.append('')

    #         items = []
    #         for u, ul, fn, da in zip(user, user_link, full_name, developer_avatars):
    #             one = {}
    #             one.setdefault('user', u)
    #             one.setdefault('user_link', ul)
    #             one.setdefault('full_name', fn)
    #             one.setdefault("developer_avatar", da)
    #             items.append(one)
    #         return {
    #             'count': len(items),
    #             'msg': 'suc',
    #             'items': items,
    #         }
    return {
        'count': 0,
        'msg': 'Unavailable.',
        'items': [],
    }

def get_soup(url, params):
    try:
        r = requests.get(url, params=params, headers=HEADER, timeout=TIMEOUT)
    except exceptions.Timeout as e:
        return False, 'timeout'
    except exceptions as b:
        return False, b
    else:
        return True, BeautifulSoup(r.text,"html.parser")


def no_trending(soup):
    is_nothing = soup.find('div', attrs={'class', 'blankslate'})
    if is_nothing is None:
        return True, "ok"
    else:
        return False, is_nothing.h3.get_text().strip()