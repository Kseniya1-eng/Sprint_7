import allure
import requests

import data


@allure.step('Создание курьера')
def create_courier(payload):
    return requests.post(f'{data.BASE_URL}{data.CREATE_COURIER_URL}', data=payload)


@allure.step('Логин курьера')
def login_courier(payload):
    return requests.post(f'{data.BASE_URL}{data.LOGIN_COURIER_URL}', data=payload)


@allure.step('Создание заказа')
def create_order(payload):
    return requests.post(f'{data.BASE_URL}{data.CREATE_ORDER_URL}', json=payload)


@allure.step('Получение списка заказов')
def get_orders():
    return requests.get(f'{data.BASE_URL}{data.LIST_ORDERS_URL}')


@allure.step('Удаление курьера')
def delete_courier(courier_id):
    return requests.delete(f'{data.BASE_URL}{data.CREATE_COURIER_URL}/{courier_id}')
