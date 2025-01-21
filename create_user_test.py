

import data
import send_request




def test_create_and_get_order():
    # Шаг 1: Выполнить запрос на создание заказа
    order_response = send_request.post_create_order(data.user_body)

    # Проверим успешность создания заказа
    assert order_response.status_code == 201, f"Ошибка при создании заказа. Код ответа: {order_response.status_code}"

    # Шаг 2: Сохранить номер трека заказа
    track_number = order_response.json().get('track')
    assert track_number is not None, "Номер трека не был возвращен в ответе"

    # Шаг 3: Выполнить запрос на получение заказа по треку заказа

    order_get_response = send_request.get_order_by_track()

    # Шаг 4: Проверить, что код ответа равен 200
    assert order_get_response.status_code == 200, f"Код ответа не равен 200. Получено: {order_get_response.status_code}"