import requests
import allure
from data import DataUser, Links, BodyResponse
from faker import Faker


class TestCreateUser:
    @allure.title('Изменение данных авторизованного пользователя')
    @allure.description('Передаем новый name, email и проверяем код 200 и что ответ содержит новые name и email')
    def test_change_data_user(self):
        fake = Faker()
        updated_data = DataUser.get_updated_data()
        headers = DataUser.get_token_user()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", headers=headers, json=updated_data)
        response_json = response.json()
        assert response.status_code == 200
        assert response_json["success"] == True
        updated_user_data = response_json.get("user", {})
        assert updated_user_data.get("email") == updated_data.get("email")
        assert updated_user_data.get("name") == updated_data.get("name")

    @allure.title('Изменение данных не авторизованного пользователя')
    @allure.description('Передаем новый name, email и проверяем код 401 и тело ответа')
    def test_change_data_user_not_authorised(self):
        updated_data = DataUser.get_updated_data()
        response = requests.patch(f"{Links.HOST}{Links.CHANGE_DATA_USER}", json=updated_data)
        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NOT_AUTHORISED
