import allure
from methods.user_methods import register_new_user
from helpers import generate_user
from data import Messages

@allure.suite("Проверка создания пользователя")
class TestCreateUser:
    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        user = generate_user()
        response = register_new_user(user['name'], user['email'], user['password'])

        assert response.status_code == 200 and response.json().get("success") is True

    @allure.title("Создать пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, register_user):
        existing_user, _, _ = register_user
        response = register_new_user(existing_user['name'], existing_user['email'], existing_user['password'])

        assert response.status_code == 403 and response.json().get("message") == Messages.USER_EXISTS_MESSAGE

    @allure.title("Создать пользователя и не заполнить одно из обязательных полей")
    def test_create_user_without_email_forbidden(self):
        user = generate_user()
        response = register_new_user(user['name'], "", user['password'])

        assert response.status_code == 403 and response.json().get("message") == Messages.EMPTY_FIELD_MESSAGE



