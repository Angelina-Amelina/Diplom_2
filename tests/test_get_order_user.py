import allure
from methods.order_methods import create_order, get_user_orders
from data import Messages


@allure.suite("Проверка получения заказов пользователя")
class TestGetOrderUser:

    @allure.title("Получение заказов конкретного пользователя: авторизованный пользователь")
    def test_get_orders_authorized_user_success(self, register_user, ingredients):
        _, _, token = register_user
        payload = {"ingredients": ingredients}
        create_order(payload, access_token=token)
        response = get_user_orders(access_token=token)

        assert response.status_code == 200 and isinstance(response.json().get("orders"), list)

    @allure.title("Получение заказов конкретного пользователя: неавторизованный пользователь")
    def test_get_orders_unauthorized_user_forbidden(self):
        response = get_user_orders(access_token=None)

        assert response.status_code == 401 and response.json().get("message") == Messages.NOT_AUTH_MESSAGE
