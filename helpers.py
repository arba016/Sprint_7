import pytest
import requests
import random
import string

from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {"login": login, "password": password, "firstName": first_name}

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(CREATE_COURIER_URL, json=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def delete_courier( payload):
        login_payload = {
            "login": payload["login"],
            "password": payload["password"],
        }

        login_response = requests.post(LOGIN_COURIER_URL, json=login_payload)

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")

def generate_random_login():
        return "ninja_" + str(random.randint(100, 9999))
