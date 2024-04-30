import requests
import allure
from helper import Helper
from data import DataUser, Links, BodyResponse


class TestCreateUser:
    @allure.title('Изменение данных name и email авторизованного пользователя')
    @allure.description('Передаем новый name, email и проверяем код 200 и что ответ содержит новые name и email')
    def test_change_data_user(self):
        updated_data = DataUser.get_updated_data()
        headers = Helper.get_token_user()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", headers=headers, json=updated_data)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["success"] == True
        updated_user_data = response_json.get("user", {})
        assert updated_user_data.get("email") == updated_data.get("email")
        assert updated_user_data.get("name") == updated_data.get("name")

    @allure.title('Изменение данных name авторизованного пользователя')
    @allure.description('Передаем новый name и проверяем код 200 и что ответ содержит новые name')
    def test_change_data_user_name(self):
        updated_data_name = DataUser.get_updated_data_name()
        headers = Helper.get_token_user()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", headers=headers, json=updated_data_name)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["success"] == True
        updated_user_data = response_json.get("user", {})
        assert updated_user_data.get("name") == updated_data_name.get("name")

    @allure.title('Изменение данных email авторизованного пользователя')
    @allure.description('Передаем новый email и проверяем код 200 и что ответ содержит новые email')
    def test_change_data_user_email(self):
        updated_data_email = DataUser.get_updated_data_email()
        headers = Helper.get_token_user()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", headers=headers, json=updated_data_email)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["success"] == True
        updated_user_data = response_json.get("user", {})
        assert updated_user_data.get("email") == updated_data_email.get("email")

    @allure.title('Изменение данных не авторизованного пользователя')
    @allure.description('Передаем новый name, email и проверяем код 401 и тело ответа')
    def test_change_data_user_not_authorised(self):
        updated_data = DataUser.get_updated_data()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", json=updated_data)
        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NOT_AUTHORISED

    @allure.title('Изменение данных name не авторизованного пользователя')
    @allure.description('Передаем новый name и проверяем код 401 и тело ответа')
    def test_change_data_user_name_not_authorised(self):
        updated_data_name = DataUser.get_updated_data_name()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", json=updated_data_name)
        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NOT_AUTHORISED

    @allure.title('Изменение данных не авторизованного пользователя')
    @allure.description('Передаем новый email и проверяем код 401 и тело ответа')
    def test_change_data_user_email_not_authorised(self):
        updated_data_email = DataUser.get_updated_data_email()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", json=updated_data_email)
        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NOT_AUTHORISED
