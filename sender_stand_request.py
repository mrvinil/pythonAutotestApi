import configuration
import data
import requests


# Определяем функцию get_docs, которая не принимает параметров
def get_docs():
    # Выполняем GET-запрос к URL, который складывается из базового URL-адреса сервиса
    # и пути к документации, заданных в модуле конфигурации
    # Функция возвращает объект ответа от сервера
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})


def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_USER_PATH объединяются для формирования полного URL для запроса
    # json=body используется для отправки данных пользователя в формате JSON
    # headers=data.headers устанавливает заголовки запроса из модуля data
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                  json=products_ids,
                  headers=data.headers)


# Вызываем функцию get_docs и сохраняем результат в переменную response
response = get_docs()
responseLogs = get_logs()
responseUsersTable = get_users_table()
responseNewUser = post_new_user(data.user_body)
responseKits = post_products_kits(data.product_ids)

# Выводим в консоль HTTP-статус код полученного ответа
# Например, 200 означает успешный запрос, 404 - не найдено и т.д.
print("get_docs:", response.status_code)
print("get_logs:", responseLogs.headers)
print("get_users_table:", responseUsersTable.status_code)
print("post_new_user:", responseNewUser.status_code)
print("post_new_user:", responseNewUser.json())
print("post_products_kits:", responseKits.status_code)
print("post_products_kits:", responseKits.json())
