import requests
from data import DataUser, Links

class Helper:
    @staticmethod
    def get_token_user():
        login_data = DataUser.creating_new_user()
        response = requests.post(f"{Links.HOST}{Links.CREATE_USER}", json=login_data)
        token = response.json().get('accessToken')
        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }
        return headers
