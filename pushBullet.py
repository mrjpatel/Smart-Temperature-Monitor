import requests
import json

"""
This class is for the push bullet logic
"""


class PushBullet:
    """
    This method is to load a PushBullet token
    """
    @classmethod
    def load_token(cls, json_file_path):
        with open(json_file_path) as json_file:
            data = json.load(json_file)
            cls.token = data['token']

    """
    This method sends the notification to PushBullet via their API
    """
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
        print("Sent Notification via PushBullet")
