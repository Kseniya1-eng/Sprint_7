import allure

import data
import helpers
import sender_requests


@allure.story('Создание курьера')
class TestCreateCourier:

    @allure.title('Курьера можно создать')
    def test_create_courier_success(self):
        payload = helpers.generate_courier_data()
        response = sender_requests.create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        # удаляем созданного курьера
        login_payload = {'login': payload['login'], 'password': payload['password']}
        courier_id = sender_requests.login_courier(login_payload).json()['id']
        sender_requests.delete_courier(courier_id)

    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_fails(self):
        payload = helpers.generate_courier_data()
        first_response = sender_requests.create_courier(payload)
        second_response = sender_requests.create_courier(payload)

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()['message'] == data.MESSAGE_COURIER_EXISTS

        # удаляем созданного курьера
        login_payload = {'login': payload['login'], 'password': payload['password']}
        courier_id = sender_requests.login_courier(login_payload).json()['id']
        sender_requests.delete_courier(courier_id)

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login_fails(self):
        response = sender_requests.create_courier(data.COURIER_WITHOUT_LOGIN)

        assert response.status_code == 400
        assert response.json()['message'] == data.MESSAGE_MISSING_CREATE_DATA

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password_fails(self):
        response = sender_requests.create_courier(data.COURIER_WITHOUT_PASSWORD)

        assert response.status_code == 400
        assert response.json()['message'] == data.MESSAGE_MISSING_CREATE_DATA

    @allure.title('Нельзя создать курьера с уже существующим логином')
    def test_create_courier_with_existing_login_fails(self):
        # создаём курьера, чтобы использовать его логин повторно
        login, password, first_name = helpers.register_new_courier_and_return_login_password()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name,
        }

        # пробуем создать курьера ещё раз с тем же логином
        response = sender_requests.create_courier(payload)

        assert response.status_code == 409
        assert response.json()['message'] == data.MESSAGE_COURIER_EXISTS

        # удаляем созданного курьера
        login_payload = {'login': login, 'password': password}
        courier_id = sender_requests.login_courier(login_payload).json()['id']
        sender_requests.delete_courier(courier_id)
