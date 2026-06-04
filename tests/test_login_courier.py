import allure
import requests
import random
import string

from data import CREATE_COURIER_URL, LOGIN_COURIER_URL, DELETE_COURIER_URL


class TestLoginCourier:

    @allure.title("Пользователь может авторизоваться")
    def test_login_courier(self, new_courier):
        response = requests.post(LOGIN_COURIER_URL, json=new_courier)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title(
        "Пользователь не может авторизоваться если при авторизации не указан login"
    )
    def test_login_without_login(self):
        payload = {"password": "password"}

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа",
        }

    @allure.title(
        "Пользователь не может авторизоваться если при авторизации не указан password"
    )
    def test_login_without_password(self, new_courier):
        payload = {"login": new_courier["login"]}

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для входа",
        }

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_courier_with_incorrect_login_and_password(self):
        payload = {
            "login": "test9870909",
            "password": "12333",
        }

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена",
        }

    @allure.title("Нельзя авторизоваться с неправильным паролем")
    def test_login_courier_with_incorrect_password(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": "wrong_password",
        }

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 404
        assert response.json() == {
            "code": 404,
            "message": "Учетная запись не найдена",
        }
