import requests
import allure
from data import IngredientOrder, Links, BodyResponse, Headers


class TestCreateOrder:
    @allure.title('Тест создания заказа авторизованным пользователем')
    @allure.description('Передаем два ингредиента и проверяем что в ответе есть "owner"')
    def test_creating_order(self):
        data = IngredientOrder.ingredient_order
        headers = Headers.get_headers()
        response = requests.post(f'{Links.HOST}{Links.CREATE_ORDER}', json=data,
                                 headers=headers)
        assert response.status_code == 200
        assert response.json().get("success") == True and "owner" in response.json()["order"]

    @allure.title('Тест создания заказа не авторизованным пользователем')
    @allure.description('Передаем два ингредиента и проверяем что в ответе есть "owner"')
    def test_creating_order_not_authorised(self):
        data = IngredientOrder.ingredient_order
        response = requests.post(f'{Links.HOST}{Links.CREATE_ORDER}', json=data)
        assert response.status_code == 200 and response.json().get("success") == True and "owner" not in response.json()

    @allure.title('Тест создания заказа без ингредиента')
    @allure.description('Не передаем в запросе "ingredients", проверяем ошибку 400 и тело ответа')
    def test_creating_order_not_ingredients(self):
        data = IngredientOrder.not_ingredient_order
        headers = Headers.get_headers()
        response = requests.post(f'{Links.HOST}{Links.CREATE_ORDER}', json=data,
                                 headers=headers)
        assert response.status_code == 400 and response.json() == BodyResponse.MESSAGE_400_NOT_INGREDIENT

    @allure.title('Тест создания заказа с неправильным ингредиентом')
    @allure.description('Не передаем в запросе "ingredients", проверяем ошибку 500 и тело ответа')
    def test_creating_order_ingredients_false(self):
        data = IngredientOrder.invalid_hash_ingredient
        headers = Headers.get_headers()
        response = requests.post(f'{Links.HOST}{Links.CREATE_ORDER}', json=data,
                                 headers=headers)
        assert response.status_code == 500
