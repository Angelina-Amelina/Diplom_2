import allure
from methods.order_methods import create_order
from data import Messages


@allure.suite("Проверка создания заказов")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_success(self, register_user, ingredients):
        _, _, token = register_user
        payload = {"ingredients": ingredients}
        response = create_order(payload, access_token=token)

        assert response.status_code == 200 and "order" in response.json()

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_without_auth_success(self, ingredients):
        payload = {"ingredients": ingredients}
        response = create_order(payload, access_token=None)

        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Ошибка создания заказа без ингредиентов")
    def test_create_order_without_ingredients_bad_request(self, register_user):
        _, _, token = register_user
        payload = {"ingredients": []}
        response = create_order(payload, access_token=token)

        assert response.status_code == 400 and response.json().get("message") == Messages.NOT_INGREDIENT_MESSAGE

    @allure.title("Ошибка сервера при создании заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash_server_error(self, register_user):
        _, _, token = register_user
        payload = {"ingredients": ["invalid_hash_123"]}
        response = create_order(payload, access_token=token)

        assert response.status_code == 500
