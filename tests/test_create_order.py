import allure
import pytest
import requests

import data
from helpers import BASE_URL


@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ можно создать с цветом: {color}')
    @pytest.mark.parametrize('color', data.OrderData.colors)
    def test_create_order_with_different_colors(self, color):
        payload = data.OrderData.build_payload(color)

        response = requests.post(f'{BASE_URL}{data.CREATE_ORDER_URL}', json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
