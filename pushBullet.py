import requests


class PushBullet:
    token = "o.2E7gXHij6qvcSNLAEsBzatiYOaw75bNm"

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
