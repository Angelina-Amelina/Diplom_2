import pytest
import allure
from methods.user_methods import change_data_user
from helpers import generate_user
from data import Messages


@allure.suite("Проверка изменения данных пользователя")
class TestChangeDataUser:

    @allure.title("Успешное изменение имени авторизованного пользователя")
    def test_change_name_with_auth_success(self, register_user):
        _, _, token = register_user
        new_user_data = generate_user()
        updated_data = {"name": new_user_data["name"]}

        response = change_data_user(updated_data, access_token=token)

        assert response.status_code == 200 and response.json().get("user", {}).get("name") == updated_data["name"]

    @allure.title("Успешное изменение email авторизованного пользователя")
    def test_change_email_with_auth_success(self, register_user):
        _, _, token = register_user
        new_user_data = generate_user()
        updated_data = {"email": new_user_data["email"]}

        response = change_data_user(updated_data, access_token=token)

        assert response.status_code == 200 and response.json().get("user", {}).get("email") == updated_data["email"]

    @allure.title("Ошибка при изменении данных неавторизованного пользователя")
    def test_change_data_without_auth_unauthorized(self, register_user):
        new_user_data = generate_user()
        updated_data = {"name": new_user_data["name"]}

        response = change_data_user(updated_data, access_token=None)

        assert response.status_code == 401 and response.json().get("message") == Messages.NOT_AUTH_MESSAGE
