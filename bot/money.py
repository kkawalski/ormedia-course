import requests

def get_money(needed):
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0"
    courses = requests.get(url).json()
    for course in courses:
    	if needed.upper() in course['Cur_Abbreviation']:
    		return "За {} курс {} BYN за {} {}".format(
                                    course['Date'][:10],
    				                course['Cur_OfficialRate'],
    				                course['Cur_Scale'],
    				                course['Cur_Abbreviation']
                                    )
    return 'Unknown money abbreviation'
