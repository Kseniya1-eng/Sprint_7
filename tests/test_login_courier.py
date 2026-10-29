import allure
import requests

import data
from helpers import BASE_URL, delete_courier, register_new_courier_and_return_login_password


@allure.story('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_courier_login_success(self):
        login, password, _ = register_new_courier_and_return_login_password()
        payload = {'login': login, 'password': password}

        response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 200
        assert 'id' in response.json()

        # удаляем созданного курьера
        courier_id = response.json()['id']
        delete_courier(courier_id)

    @allure.title('Нельзя авторизоваться без логина')
    def test_courier_login_without_login_fails(self):
        payload = {'password': data.generate_random_string(10)}
        response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для входа'

    @allure.title('Нельзя авторизоваться без пароля')
    def test_courier_login_without_password_fails(self):
        payload = {'login': data.generate_random_string(10)}
        response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)

        # известная особенность сервиса: при отсутствии пароля возвращается 504
        assert response.status_code == 504

    @allure.title('Нельзя авторизоваться с неправильным паролем')
    def test_courier_login_with_wrong_password_fails(self):
        login, password, _ = register_new_courier_and_return_login_password()
        payload = {'login': login, 'password': 'wrong_password'}

        response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'

        # удаляем созданного курьера, используя правильный пароль
        login_response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}',
                                       data={'login': login, 'password': password})
        courier_id = login_response.json()['id']
        delete_courier(courier_id)

    @allure.title('Нельзя авторизоваться под несуществующим пользователем')
    def test_courier_login_with_nonexistent_user_fails(self):
        payload = {
            'login': data.generate_random_string(10),
            'password': data.generate_random_string(10),
        }
        response = requests.post(f'{BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)

        assert response.status_code == 404
        assert response.json()['message'] == 'Учетная запись не найдена'
