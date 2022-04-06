import requests
from pprint import pprint

with open('TOKEN_yandex.txt', encoding='utf-8') as file:
    TOKEN = file.read()
    print()

class Yandex:
    url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def __init__(self, token):
        self.token = token

    def create_folder(self, folder_name):
        headers = {'Content-Type': 'application/json',
                   'Accept': 'application/json',
                   'Authorization': f'OAuth {self.token}'}
        params = {'path': folder_name}
        response = requests.put(url=self.url, params=params, headers=headers).status_code
        return response

user_yandex = Yandex(TOKEN)

