import requests
import allure
from urls import Urls

@allure.step('Получение данных об ингредиентах')
def ingredients_info():
    return requests.get(Urls.INGREDIENTS)

@allure.step('Создание заказа')
def create_order(payload, access_token=""):
    headers = {"Authorization": access_token} if access_token else {}
    return requests.post(Urls.ORDERS, json=payload, headers=headers)

@allure.step('Получение заказов пользователя')
def get_user_orders(access_token=""):
    headers = {"Authorization": access_token} if access_token else {}
    return requests.get(Urls.ORDERS, headers=headers)