import allure
import requests

import data
from helpers import BASE_URL


@allure.story('Список заказов')
class TestListOrders:

    @allure.title('В тело ответа возвращается список заказов')
    def test_list_orders_returns_list(self):
        response = requests.get(f'{BASE_URL}{data.LIST_ORDERS_URL}')

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0
