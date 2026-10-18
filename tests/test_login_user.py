import allure
from methods.user_methods import login_user
from helpers import generate_user
from data import Messages

@allure.suite("Проверка авторизации пользователя")
class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user_success(self, register_user):
        user, _, _ = register_user
        login_data = {
            "email": user["email"],
            "password": user["password"]
        }
        response = login_user(login_data)

        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Логин с неверным логином и паролем")
    def test_login_with_incorrect_field(self):
        incorrect_user = generate_user()
        login_data = {
            "email": incorrect_user["email"],
            "password": incorrect_user["password"]
        }
        response = login_user(login_data)

        assert response.status_code == 401 and response.json().get("message") == Messages.INCORRECT_LOGIN_FIELD_MESSAGE