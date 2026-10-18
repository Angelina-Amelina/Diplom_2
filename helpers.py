import random
import string

def generate_user():
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return {
        "email": f"lina_test_{random_str}@yandex.ru",
        "password": f"pass_{random_str}",
        "name": f"lina_{random_str}"
    }