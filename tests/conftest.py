import pytest
from methods.user_methods import register_new_user, delete_user
from methods.order_methods import ingredients_info
from helpers import generate_user

@pytest.fixture
def register_user():
    user = generate_user()
    response = register_new_user(user['name'], user['email'], user['password'])
    token = response.json().get("accessToken") if response.status_code == 200 else None
    yield user, response, token

    if token:
        delete_user(token)

@pytest.fixture
def all_ingredients():
    response = ingredients_info()
    return response.json().get("data", [])

@pytest.fixture
def ingredient(all_ingredients):
    return all_ingredients[0]["_id"] if all_ingredients else None

@pytest.fixture
def ingredients(all_ingredients):
    if len(all_ingredients) >= 2:
        return [all_ingredients[0]["_id"], all_ingredients[1]["_id"]]
    elif all_ingredients:
        return [all_ingredients[0]["_id"]]
    return []