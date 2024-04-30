import pytest
import requests
import allure
from data import DataUser, Links, BodyResponse


class TestCreateUser:
    @allure.title('Тест создания уникального пользователя')
    @allure.description(
        'Генерируем рандомный name, email, password и передаем запрос с корректными параметрами, проверяем код 200 и '
        'тело ответа')
    def test_creating_user(self):
        data = DataUser.creating_new_user()
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Тест нельзя создать двух одинаковых пользователей')
    @allure.description(
        'В данных передаем email и password, который был ранее зарегистрирован. Проверяем код 403 и тело ответа.')
    @pytest.mark.parametrize("name, email, password", [
        ("ivan_0052", "ivan_0052@test.ru", "qwerrty1234"),
        ("ivan_00052", "ivan_0052@test.ru", "qwerrty1234"),
        ("ivan_0052", "ivan_0052@test.ru", "qwerrty01234"),
    ])
    def test_creating_user_double(self, name, email, password):
        description = f"В данных передаем name '{name}' email '{email}' и password '{password}', который был ранее " \
                      f"зарегистрирован."
        allure.dynamic.description(description)

        data = {
            "name": name,
            "email": email,
            "password": password
        }
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)
        assert response.status_code == 403 and response.json() == BodyResponse.MESSAGE_403_DOUBLE_USER

    @allure.title('Тест на авторизацию без указания имени, email или пароля')
    @pytest.mark.parametrize("name, email, password", [
        ("", "kurochkin@test.ru", "1234"),
        ("kurochkin", "", "1234"),
        ("kurochkin", "kurochkin@test.ru", "")
    ])
    def test_authentication_without_name_or_email_or_password(self, name, email, password):
        description = f"Тест на авторизацию без указания имени='{name}', email='{email}', пароля='{password}'"
        allure.dynamic.description(description)

        data = {
            "name": name,
            "email": email,
            "password": password
        }
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)

        assert response.status_code == 403 and response.json() == BodyResponse.MESSAGE_403_NONE_VALUE
