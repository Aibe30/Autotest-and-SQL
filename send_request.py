#Соколовский Андрей Валерьевич, QA25 Финальный проект. Инженер по тестированию плюс.
import requests
import data
import configuration
#1Создаем заказ
def post_create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER, json=body, headers=data.headers)
response = post_create_order(data.user_body)
print(response.status_code)

if response.status_code != 201:
    raise Exception("Что-то пошло не так.")
else:
    print("Заказ успешно создан!")
#2 Присваиваем номер заказа
post_track_number = response.json()['track']
print(post_track_number)
#3 Получаем заказ по номеру
def get_order_by_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
                        params={'track': post_track_number})
response = get_order_by_track()
print(response.status_code)
#4 Проверка что код ответа 200
assert response.status_code == 200, f'Ожидался код ответа 200, но получен {response.status_code}. Ошибка: {response.text}'






