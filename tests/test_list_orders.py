import allure

import data
import sender_requests


@allure.story('Список заказов')
class TestListOrders:

    @allure.title('В тело ответа возвращается список заказов')
    def test_list_orders_returns_list(self):
        response = sender_requests.get_orders()

        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0
