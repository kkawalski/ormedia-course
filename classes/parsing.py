import requests
from bs4 import BeautifulSoup
import json

def get_html(url):
	r = requests.get(url)
	return r.text

def get_data(html):
	courses = json.loads(html)
	return courses

def main():
	url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
	courses = get_data(get_html(url))
	needed = 'Йен'
	for course in courses:
		if needed in course['Cur_Name']:
			print("За {} курс {} BYN за {} {}".format(course['Date'][:10],
													course['Cur_OfficialRate'],
													course['Cur_Scale'],
													course['Cur_Abbreviation']))
			pass
	print('Error')

"""
def get_course(html):
	soup = BeautifulSoup(html, 'lxml')
	course = soup.find('div', id='ratesData').find('table').find_all('td')
	return course

def get_date(html):
	soup = BeautifulSoup(html, 'lxml')
	date = soup.find('span', id="curDate").text
	return date

def main():
	url = "http://www.nbrb.by/statistics/Rates/RatesDaily.asp"
	course_list = get_course(get_html(url))

	name = [el.text.strip() for el in course_list[::3]]
	count = [el.text.strip() for el in course_list[1::3]]
	course = [el.text.strip() for el in course_list[2::3]]

	courses = {key: value for key, value in list(zip(name, list(zip(count, course))))}

	needed = 'Евро'

	print("За {} курс {} BYN за {}".format(get_date(get_html(url)), courses[needed][1], courses[needed][0]))
"""

if __name__ == '__main__':
	main()
