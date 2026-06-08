import allure
import requests

from data import GET_ORDERS_URL


class TestOrders:

    @allure.title("Получение списка заказов")
    def test_get_all_orders(self):

        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
