import allure
import requests
import pytest
from data import LOGIN_COURIER_URL, COURIER_NOT_FOUND_ERROR, LOGIN_REQUIRED_FIELDS_ERROR_MESSAGE, WITHOUT_LOGIN, WITHOUT_PASSWORD


class TestLoginCourier:

    @allure.title("Пользователь может авторизоваться")
    def test_login_courier(self, new_courier):
        response = requests.post(LOGIN_COURIER_URL, json=new_courier)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title(
        "Пользователь не может авторизоваться если не указано обязательное поле"
    )
    @pytest.mark.parametrize("payload", [WITHOUT_LOGIN, WITHOUT_PASSWORD])
    def test_login_without_required_field(self, payload):

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert response.json()["message"] == LOGIN_REQUIRED_FIELDS_ERROR_MESSAGE

    @allure.title("Нельзя авторизоваться под несуществующим пользователем")
    def test_login_courier_with_incorrect_login_and_password(self):
        payload = {
            "login": "test9870909",
            "password": "12333",
        }

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND_ERROR

    @allure.title("Нельзя авторизоваться с неправильным паролем")
    def test_login_courier_with_incorrect_password(self, new_courier):
        payload = {
            "login": new_courier["login"],
            "password": "wrong_password",
        }

        response = requests.post(LOGIN_COURIER_URL, json=payload)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND_ERROR
