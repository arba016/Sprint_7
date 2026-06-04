import pytest
import requests

from helpers import register_new_courier_and_return_login_password, delete_courier



@pytest.fixture
def new_courier():
    login_pass = register_new_courier_and_return_login_password()

    assert login_pass, "Курьер не был создан"

    payload = {
        "login": login_pass[0],
        "password": login_pass[1],
    }

    yield payload

    delete_courier(payload)