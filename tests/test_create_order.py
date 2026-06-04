import requests
import pytest
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
    def test_create_order_black_scooter(self, color):

        response = requests.post(CREATE_ORDER_URL, json=color)

        assert response.status_code == 201
        assert "track" in response.json()
