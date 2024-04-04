from faker import Faker
import requests


class Links:
    HOST = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = "/api/auth/register"
    LOGIN = "/api/auth/login"
    CHANGE_DATA_USER = "/api/auth/user"
    CREATE_ORDER = "/api/orders"
    GET_ORDER_USER = "/api/orders"


class DataUser:
    fake = Faker()
    name = fake.name()
    password = fake.password()
    email = fake.email()

    creating_new_user = {"email": email,
                         "password": password,
                         "name": name}

    creating_double_user = {"email": 'ivan_0052@test.ru',
                            "password": 'qwerrty1234',
                            "name": 'ivan_0052'}

    user = {"email": 'ivan_0052@test.ru',
            "password": 'qwerrty1234'
            }

    @staticmethod
    def get_token_user():
        login_data = DataUser.creating_new_user
        response = requests.post(f"{Links.HOST}{Links.CREATE_USER}", json=login_data)
        token = response.json().get('accessToken')
        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def get_updated_data():
        fake = Faker()
        updated_data = {"email": fake.email(),
                        "name": fake.name()}
        return updated_data


class IngredientOrder:
    ingredient_order = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                        "609646e4dc916e00276b2870"]}
    not_ingredient_order = {}
    invalid_hash_ingredient = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                               "609646e4dc916e00276b287"]}


class Headers:
    @staticmethod
    def get_headers():
        login_data = DataUser.user
        response = requests.post(f"{Links.HOST}{Links.LOGIN}", json=login_data)
        token = response.json().get('accessToken')
        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }
        return headers

    @staticmethod
    def get_data_new_user():
        login_data = DataUser.creating_new_user
        response = requests.post(f"{Links.HOST}{Links.LOGIN}", json=login_data)
        token = response.json().get('accessToken')
        headers = {
            'Authorization': f'{token}',
            'Content-Type': 'application/json'
        }
        return headers


class BodyResponse:
    MESSAGE_403_DOUBLE_USER = {
        "success": False,
        "message": "User already exists"
    }
    MESSAGE_403_NONE_VALUE = {
        "success": False,
        "message": "Email, password and name are required fields"}
    MESSAGE_401_NONE_VALUE_IN_FIELD = {
        "success": False,
        "message": "email or password are incorrect"}
    MESSAGE_400_NOT_INGREDIENT = {
        "success": False,
        "message": "Ingredient ids must be provided"}
    MESSAGE_401_NOT_AUTHORISED = {
        "success": False,
        "message": "You should be authorised"
    }
