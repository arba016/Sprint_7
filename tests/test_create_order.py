import requests
import pytest
import allure
from data import (
    CREATE_ORDER_URL,
    ORDER_GREY_SCOOTER,
    ORDER_BLACK_SCOOTER,
    ORDER_WITHOUT_COLOR_SCOOTER,
    ORDER_BLACK_AND_GRAY_SCOOTER,
)


class TestCreateOrder:

    @pytest.mark.parametrize(
        "color",
        [
            (ORDER_GREY_SCOOTER),
            (ORDER_BLACK_SCOOTER),
            (ORDER_WITHOUT_COLOR_SCOOTER),
            (ORDER_BLACK_AND_GRAY_SCOOTER),
        ],
    )
    @allure.title("Создание заказа самоката с разными вариантами цвета")
    def test_create_order_scooter(self, color):

        response = requests.post(CREATE_ORDER_URL, json=color)

        assert response.status_code == 201
        assert "track" in response.json()
