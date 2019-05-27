import requests

def get_money(needed):
    url = "http://www.nbrb.by/API/ExRates/Rates?Periodicity=0" #json с курсами валют за сегодня
    courses = requests.get(url).json()
    for course in courses:
    	if needed.upper() in course['Cur_Abbreviation']: # ищем запрашиваемую валюту
    		return "За {} курс {} BYN за {} {}".format( 
                                    course['Date'][:10],
    				                course['Cur_OfficialRate'],
    				                course['Cur_Scale'],
    				                course['Cur_Abbreviation']
                                    ) #если нашли, возвращаем строку в таком формате
    return 'Unknown money abbreviation' #если не нашли, возврщаем сообщение, что валют нет
