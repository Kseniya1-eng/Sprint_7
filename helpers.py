import allure
import random
import string

import sender_requests


@allure.step('Генерация случайной строки')
def generate_random_string(length):
    """Возвращает строку из букв нижнего регистра заданной длины."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Генерация данных нового курьера')
def generate_courier_data():
    """Возвращает словарь с логином, паролем и именем нового курьера."""
    return {
        'login': generate_random_string(10),
        'password': generate_random_string(10),
        'firstName': generate_random_string(10),
    }


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
@allure.step('Регистрация нового курьера и получение логина и пароля')
def register_new_courier_and_return_login_password():
    # собираем тело запроса
    payload = generate_courier_data()

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = sender_requests.create_courier(payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        return [payload['login'], payload['password'], payload['firstName']]

    # возвращаем пустой список
    return []
