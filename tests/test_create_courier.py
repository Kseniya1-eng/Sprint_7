import allure
import requests

import data
from helpers import BASE_URL, delete_courier, register_new_courier_and_return_login_password


@allure.story('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        payload = data.CourierData.full_payload()
        response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # удаляем созданного курьера
        login_response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)
        courier_id = login_response.json()['id']
        delete_courier(courier_id)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_fails(self):
        payload = data.CourierData.full_payload()
        first_response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)
        second_response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

        # удаляем созданного курьера
        login_response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)
        courier_id = login_response.json()['id']
        delete_courier(courier_id)

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_fails(self):
        payload = data.CourierData.build_payload(password='some_password', firstName='SomeName')
        response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password_fails(self):
        payload = data.CourierData.build_payload(login='some_login', firstName='SomeName')
        response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Нельзя создать курьера с уже существующим логином')
    def test_create_courier_with_existing_login_fails(self):
        # создаём курьера, чтобы использовать его логин повторно
        login, password, first_name = register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name,
        }

        # пробуем создать курьера ещё раз с тем же логином
        response = requests.post(f'{BASE_URL}{data.CREATE_COURIER_URL}', data=payload)

        assert response.status_code == 409
        assert response.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

        # удаляем созданного курьера
        login_response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)
        courier_id = login_response.json()['id']
        delete_courier(courier_id)
