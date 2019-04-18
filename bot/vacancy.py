import requests
from bs4 import BeautifulSoup as bs

def tut_parse(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    soup = bs(request.content, 'lxml')
    divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_premium'}) + soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'})
    for div in divs:
        title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
        href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
        company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
        responsibility = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
        requirement = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
        content = responsibility + ' ' + requirement
        jobs.append({
            'title': title,
            'href': href,
            'company': company,
            'content': content,
        })
    return jobs
