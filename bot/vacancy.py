import requests
from bs4 import BeautifulSoup as bs

def tut_parse(base_url, headers):
    jobs = []
    session = requests.Session() #объект с параметрами запроса
    request = session.get(base_url, headers=headers) #ссылка на страницу с вакансиями
    soup = bs(request.content, 'lxml') 
    divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_premium'}) + soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy'}) #ищем заданные дивы в верстке
    for div in divs: #из каждого блока с вакансиями берем заголовок, ссылку, название компании, требования
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
        })# список с вакансиями
    return jobs
