BASE_URL = 'https://qa-scooter.praktikum-services.ru'

CREATE_COURIER_URL = '/api/v1/courier'
LOGIN_COURIER_URL = '/api/v1/courier/login'
CREATE_ORDER_URL = '/api/v1/orders'
LIST_ORDERS_URL = '/api/v1/orders'

# --- Заказ: базовое тело запроса (без цвета) ---
ORDER_BODY = {
    'firstName': 'Иван',
    'lastName': 'Иванов',
    'address': 'Москва, ул. Ленина, д. 1',
    'metroStation': '4',
    'phone': '+79991112233',
    'rentTime': 5,
    'deliveryDate': '2026-11-05',
    'comment': 'Тестовая доставка',
}

# --- Заказ: варианты с цветом для параметризации ---
ORDER_BLACK = {**ORDER_BODY, 'color': ['BLACK']}
ORDER_GREY = {**ORDER_BODY, 'color': ['GREY']}
ORDER_BOTH = {**ORDER_BODY, 'color': ['BLACK', 'GREY']}
ORDER_NO_COLOR = {**ORDER_BODY, 'color': []}

# список вариантов заказа для параметризации
ORDER_VARIANTS = [ORDER_BLACK, ORDER_GREY, ORDER_BOTH, ORDER_NO_COLOR]

# --- Курьер: тело запроса без одного из обязательных полей ---
COURIER_WITHOUT_LOGIN = {'password': 'courier_password', 'firstName': 'courier_name'}
COURIER_WITHOUT_PASSWORD = {'login': 'courier_login', 'firstName': 'courier_name'}

# --- Логин: тело запроса без одного из полей ---
LOGIN_WITHOUT_LOGIN = {'password': 'courier_password'}
LOGIN_WITHOUT_PASSWORD = {'login': 'courier_login'}

# --- Ожидаемые сообщения об ошибках ---
MESSAGE_COURIER_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
MESSAGE_MISSING_CREATE_DATA = 'Недостаточно данных для создания учетной записи'
MESSAGE_MISSING_LOGIN_DATA = 'Недостаточно данных для входа'
MESSAGE_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
