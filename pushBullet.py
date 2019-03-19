import requests
import json


class PushBullet:
    @classmethod
    def loadToken(cls, jsonFilePath):
        with open(jsonFilePath) as json_file:
            data = json.load(json_file)
            cls.token = data['token']

    @classmethod
    def notify(cls, message):
        data = {
            'type': 'note',
            'title': 'Alert',
            'body': message
        }
        response = requests.post(
            'https://api.pushbullet.com/v2/pushes',
            data=data,
            auth=(cls.token, '')
        )
