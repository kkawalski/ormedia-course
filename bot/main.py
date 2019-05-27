from base import BaseBot
from money import get_money
from config import token
import vacancy
from random import randint

def main(money_bot):
    new_offset = None

    headers = {
            'accept': '*/*',
            'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
            } #для имитации работы браузера
    vacancy_url = 'https://jobs.tut.by/search/vacancy?area=1002&text=python&page=0'
    jobs = vacancy.tut_parse(vacancy_url, headers) #список вакансий на первой странице тут бая

    while True:
        money_bot.get_updates(offset=new_offset) #получили начальные обновления

        last_update = money_bot.get_last_update() #получили последнее

        answer = money_bot.get_message() #считали сообщение для бота
        chat_id = answer['chat_id'] #чат айди пользователя
        text = answer['text'] #текст, отправеленный пользователем

        if text[0] == '/': #команды начинаются с /
            if text[1:] == 'vacancy': #запрос вакансий
                job = jobs[randint(0, len(jobs)-1)] #выбираем случайную вакансию с первой страницы
                mess = "{}\n{}\n{}\n{}".format(job['title'], job['href'], job['company'], job['content'])
                money_bot.send_message(chat_id, mess) #отправляем сообщение пользователю, который запросил(по chat_id)
            else:
                money_bot.send_message(chat_id, get_money(text[1:])) #в противнов случае считаем команду аббревиатурой валюты и отправляем ее курс
        else:
            money_bot.send_message(chat_id, 'Command starts with "/"')

        new_offset = last_update['update_id'] + 1 #смещаем идентификатор первого возвращаемого обновления(должен быть на 1 больше чем последнее(так написано в апи телеги))


if __name__ == '__main__':
    money_bot = BaseBot(token)
    try:
        main(money_bot)
    except:
        exit()
