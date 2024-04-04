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
        data = DataUser.creating_new_user
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Тест нельзя создать двух одинаковых пользователей')
    @allure.description('В данных передаем email и password который был ранее зарегистрирован, проверяем код 403 и тело'
                        'ответа')
    def test_creating_user_double(self):
        data = DataUser.creating_double_user
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)
        assert response.status_code == 403 and response.json() == BodyResponse.MESSAGE_403_DOUBLE_USER

    @allure.title('Тест если при авторизации какого-то поля нет, запрос возвращает ошибку 403')
    @allure.description('Передаем данные сначала без name потом email потом password, проверяем код и тело'
                        'ответа')
    @pytest.mark.parametrize("name, email, password", [
        ("", "kurochkin@test.ru", "1234"),
        ("kurochkin", "", "1234"),
        ("kurochkin", "kurochkin@test.ru", "")
    ])
    def test_authentication_without_name_or_email_or_password(self, name, email, password):
        data = {
            "name": name,
            "email": email,
            "password": password
        }
        response = requests.post(f'{Links.HOST}{Links.CREATE_USER}', json=data)

        assert response.status_code == 403 and response.json() == BodyResponse.MESSAGE_403_NONE_VALUE
