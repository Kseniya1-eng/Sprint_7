import allure

import data
import helpers
import sender_requests


@allure.story('Логин курьера')
class TestLoginCourier:

    @allure.title('Курьер может авторизоваться')
    def test_courier_login_success(self):
        login, password, _ = helpers.register_new_courier_and_return_login_password()

        response = sender_requests.login_courier({'login': login, 'password': password})

        assert response.status_code == 200
        assert 'id' in response.json()

        # удаляем созданного курьера
        courier_id = response.json()['id']
        sender_requests.delete_courier(courier_id)

    @allure.title('Нельзя авторизоваться без логина')
    def test_courier_login_without_login_fails(self):
        response = sender_requests.login_courier(data.LOGIN_WITHOUT_LOGIN)

        assert response.status_code == 400
        assert response.json()['message'] == data.MESSAGE_MISSING_LOGIN_DATA

    @allure.title('Нельзя авторизоваться без пароля')
    def test_courier_login_without_password_fails(self):
        response = sender_requests.login_courier(data.LOGIN_WITHOUT_PASSWORD)

        # известная особенность сервиса: при отсутствии пароля возвращается 504
        assert response.status_code == 504

    @allure.title('Нельзя авторизоваться с неправильным паролем')
    def test_courier_login_with_wrong_password_fails(self):
        login, password, _ = helpers.register_new_courier_and_return_login_password()

        response = sender_requests.login_courier({'login': login, 'password': 'wrong_password'})

        assert response.status_code == 404
        assert response.json()['message'] == data.MESSAGE_ACCOUNT_NOT_FOUND

        # удаляем созданного курьера, используя правильный пароль
        login_payload = {'login': login, 'password': password}
        courier_id = sender_requests.login_courier(login_payload).json()['id']
        sender_requests.delete_courier(courier_id)

    @allure.title('Нельзя авторизоваться под несуществующим пользователем')
    def test_courier_login_with_nonexistent_user_fails(self):
        login_payload = {
            'login': helpers.generate_random_string(10),
            'password': helpers.generate_random_string(10),
        }
        response = sender_requests.login_courier(login_payload)

        assert response.status_code == 404
        assert response.json()['message'] == data.MESSAGE_ACCOUNT_NOT_FOUND
