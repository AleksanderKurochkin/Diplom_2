import requests
import allure
from data import IngredientOrder, Links, BodyResponse, Headers


class TestCreateOrder:
    @allure.title('Тест получения заказов авторизованного пользователя')
    @allure.description('Передаем токен и проверяем ответ код 200')
    def test_order_user(self):
        headers = Headers.get_headers()
        response = requests.get(f'{Links.HOST}{Links.GET_ORDER_USER}',
                                headers=headers)
        assert response.status_code == 200 and response.json().get("success") == True

    @allure.title('Тест получения заказа не авторизованным пользователем')
    @allure.description('Передаем два ингредиента и проверяем что в ответе есть "owner"')
    def test_creating_order(self):
        data = IngredientOrder.ingredient_order
        response = requests.get(f'{Links.HOST}{Links.GET_ORDER_USER}')
        assert response.status_code == 401 and response.json() == BodyResponse.MESSAGE_401_NOT_AUTHORISED
