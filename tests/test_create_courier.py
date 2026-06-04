import allure
import requests
import pytest

from data import CREATE_COURIER_URL, WITHOUT_PASSWORD, WITHOUT_LOGIN, COURIER_REQUIRED_FIELDS_ERROR, RESPONSE_JSON_MESSAGE_OK, COURIER_ALREADY_EXISTS_ERROR
from helpers import delete_courier, generate_random_login


class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_courier_can_be_created(self):
        payload = {
            "login": generate_random_login(),
            "password": "1234",
            "firstName": "saske",
        }

        try:
            response = requests.post(CREATE_COURIER_URL, json=payload)

            assert response.status_code == 201
            assert response.json() == RESPONSE_JSON_MESSAGE_OK

        finally:
            delete_courier(payload)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_courier_cannot_be_created_twice(self):
        payload = {
            "login": generate_random_login(),
            "password": "1234",
            "firstName": "saske",
        }

        try:
            first_response = requests.post(CREATE_COURIER_URL, json=payload)
            second_response = requests.post(CREATE_COURIER_URL, json=payload)

            assert first_response.status_code == 201
            assert first_response.json() == RESPONSE_JSON_MESSAGE_OK

            assert second_response.status_code == 409
            assert (
                second_response.json()["message"]
                == COURIER_ALREADY_EXISTS_ERROR
            )

        finally:
            delete_courier(payload)

    @pytest.mark.parametrize("payload", [WITHOUT_LOGIN, WITHOUT_PASSWORD])
    @allure.title("Нельзя создать курьера без обязательного поля")
    def test_courier_cannot_be_created_without_required_field(self, payload):
        response = requests.post(CREATE_COURIER_URL, json=payload)

        assert response.status_code == 400
        assert (
            response.json()["message"]
            == COURIER_REQUIRED_FIELDS_ERROR
        )