import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru'

CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
LIST_ORDERS_URL = '/api/v1/orders'


# метод генерирует строку, состоящую только из букв нижнего регистра
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class CourierData:
    """Данные и методы для создания и логина курьера."""

    @staticmethod
    def full_payload():
        """Тело запроса со всеми обязательными полями."""
        return {
            'login': generate_random_string(10),
            'password': generate_random_string(10),
            'firstName': generate_random_string(10),
        }

    @staticmethod
    def build_payload(**overrides):
        """Собирает тело запроса и позволяет убрать/изменить любое поле."""
        payload = CourierData.full_payload()
        payload.pop('login')
        payload.pop('password')
        payload.pop('firstName')
        payload.update(overrides)
        return payload


class OrderData:
    """Данные и методы для создания заказа."""

    # варианты цветов самоката: только BLACK, только GREY, оба или ни одного
    colors = [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        [],
    ]

    @staticmethod
    def build_payload(color):
        """Собирает тело заказа с переданным списком цветов."""
        return {
            'firstName': 'Иван',
            'lastName': 'Иванов',
            'address': 'Москва, ул. Ленина, д. 1',
            'metroStation': '4',
            'phone': '+79991112233',
            'rentTime': 5,
            'deliveryDate': '2026-11-05',
            'comment': 'Тестовая доставка',
            'color': color,
        }
