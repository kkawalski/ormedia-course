import requests

class BaseBot:

    def __init__(self, token):
        self.token = token
        self.url = 'https://api.telegram.org/bot{}/'.format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.url + method, params)
        return resp.json()['result']

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        resp = requests.post(self.url + method, params)
        return resp

    def get_message(self):
        data = self.get_last_update()
        chat_id = data['message']['chat']['id']
        message_text = data['message']['text']
        message = {
                    'chat_id': chat_id,
                    'text': message_text,
                   }
        return message

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update
