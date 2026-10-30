import allure
import pytest

import data
import sender_requests


@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Заказ можно создать с цветом: {color}')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []],
                             ids=['black', 'grey', 'both', 'none'])
    def test_create_order_with_different_colors(self, color):
        payload = {**data.ORDER_BODY, 'color': color}

        response = sender_requests.create_order(payload)

        assert response.status_code == 201
        assert 'track' in response.json()
