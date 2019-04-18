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
            }
    vacancy_url = 'https://jobs.tut.by/search/vacancy?area=1002&text=python&page=0'
    jobs = vacancy.tut_parse(vacancy_url, headers)

    while True:
        money_bot.get_updates(offset=new_offset)

        last_update = money_bot.get_last_update()

        answer = money_bot.get_message()
        chat_id = answer['chat_id']
        text = answer['text']

        if text[0] == '/':
            if text[1:] == 'vacancy':
                job = jobs[randint(0, len(jobs)-1)]
                mess = "{}\n{}\n{}\n{}".format(job['title'], job['href'], job['company'], job['content'])
                money_bot.send_message(chat_id, mess)
            else:
                money_bot.send_message(chat_id, get_money(text[1:]))
        else:
            money_bot.send_message(chat_id, 'Command starts with "/"')

        new_offset = last_update['update_id'] + 1


if __name__ == '__main__':
    money_bot = BaseBot(token)
    try:
        main(money_bot)
    except:
        exit()
