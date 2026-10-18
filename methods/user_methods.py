import requests
import allure
from urls import Urls

@allure.step('Регистрация нового пользователя')
def register_new_user(name, email, password):
    data = {
        'email': email,
        'password': password,
        'name': name
    }
    return requests.post(Urls.USER_REGISTER, json=data)


@allure.step('Удаление существующего юзера')
def delete_user(access_token):
    headers = {"Authorization": access_token} if access_token else {}
    return requests.delete(Urls.USER_DATA, headers=headers)


@allure.step('Авторизация пользователя')
def login_user(login_data):
    return requests.post(Urls.USER_LOGIN, json=login_data)


@allure.step('Изменение данных аккаунта')
def change_data_user(updated_info, access_token=""):
    headers = {"Authorization": access_token} if access_token else {}
    return requests.patch(Urls.USER_DATA, json=updated_info, headers=headers)

