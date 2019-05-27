import requests

class BaseBot:

    def __init__(self, token):
        self.token = token
        self.url = 'https://api.telegram.org/bot{}/'.format(token) 

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates' #метод для апи
        params = {'timeout': timeout, 'offset': offset} #тамй-аут для лонг поллинга(сервер может не сразу оветить), оффсет - идентификатор первого возвращаемого обновления
        resp = requests.get(self.url + method, params) #запрашиваем обновления
        return resp.json()['result'] #возврщаем поле результата из словаря

    def send_message(self, chat_id, text):
        method = 'sendMessage' #метод для апи
        params = {'chat_id': chat_id, 'text': text} #айди чата с пользователем, текст отправленный пользователю
        resp = requests.post(self.url + method, params) #отправление сообщения пользователю
        return resp

    def get_message(self): #достаем сообщение из последнего обновления
        data = self.get_last_update()
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']
        message = {
                    'chat_id': chat_id,
                    'text': message_text,
                   }
        return message

    def get_last_update(self): #берем последнее обновление
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
