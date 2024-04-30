import pytest
import requests
import allure
from data import DataUser, Links, BodyResponse


class TestLoginUser:
    @allure.title('Тест юзер может авторизоваться')
    @allure.description('Передаем корректные данные, проверяем код 200')
    def test_courier_authentication_success(self):
        data = DataUser.user
        response = requests.post(f'{Links.HOST}{Links.LOGIN}', json=data)

        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Тест на авторизацию без указания email или пароля')
    @allure.description('Передаем данные сначала без email, затем без password, также проверяем некорректные данные')
    @pytest.mark.parametrize("email, password", [
        ("ivan_0052@test.ru", ""),
        ("", "qwerrty1234"),
        ("ivan_0052@test", "qwerrty1234"),
        ("ivan_0052@test.ru", "qw")
    ])
    def test_authentication_without_login_or_password(self, email, password):
        description = f"Тест на авторизацию без указания email='{email}' или пароля='{password}'"
        allure.dynamic.description(description)

        data = {
            "email": email,
            "password": password
        }
        response = requests.post(f'{Links.HOST}{Links.LOGIN}', json=data)

        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NONE_VALUE_IN_FIELD

