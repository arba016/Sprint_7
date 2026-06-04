import allure
import requests
import random
import string

from data import CREATE_COURIER_URL, DELETE_COURIER_URL, LOGIN_COURIER_URL


class TestCreateCourier:

    def delete_courier(self, payload):
        login_payload = {
            "login": payload["login"],
            "password": payload["password"],
        }

        login_response = requests.post(LOGIN_COURIER_URL, json=login_payload)

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f"{DELETE_COURIER_URL}/{courier_id}")

    def generate_random_login(self):
        return "ninja_" + str(random.randint(100, 9999))

    @allure.title("Курьера можно создать")
    def test_courier_can_be_created(self):
        payload = {
            "login": self.generate_random_login(),
            "password": "1234",
            "firstName": "saske",
        }

        try:
            response = requests.post(CREATE_COURIER_URL, json=payload)

            assert response.status_code == 201
            assert response.json() == {"ok": True}

        finally:

            self.delete_courier(payload)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_courier_cannot_be_created_twice(self):
        payload = {
            "login": self.generate_random_login(),
            "password": "1234",
            "firstName": "saske",
        }

        try:
            first_response = requests.post(CREATE_COURIER_URL, json=payload)
            second_response = requests.post(CREATE_COURIER_URL, json=payload)

            assert first_response.status_code == 201
            assert first_response.json() == {"ok": True}

            assert second_response.status_code == 409
            assert (
                second_response.json()["message"]
                == "Этот логин уже используется. Попробуйте другой."
            )

        finally:
            self.delete_courier(payload)

    @allure.title("Нельзя создать пользователя если нет обязательного поля login")
    def test_courier_cannot_be_created_without_login(self):
        payload = {
            "password": "1234",
            "firstName": "saske",
        }

        response = requests.post(CREATE_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи",
        }

    @allure.title("Нельзя создать пользователя если нет обязательного поля password")
    def test_courier_cannot_be_created_without_password(self):
        payload = {
            "login": self.generate_random_login(),
            "firstName": "saske",
        }

        response = requests.post(CREATE_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert response.json() == {
            "code": 400,
            "message": "Недостаточно данных для создания учетной записи",
        }
