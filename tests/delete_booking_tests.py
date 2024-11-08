import booking_api
import data


def test_delete_booking_success():
    # Arrange
    create_request = booking_api.create_booking(data.CREATE_BOOKING_BODY)
    token_request = booking_api.auth(data.AUTH_BOOKING_BODY)

    # Достаем данные из ответа сервера
    booking_id = create_request.json()['bookingid']
    token = token_request.json()['token']

    # Act
    delete_request = booking_api.delete_booking(booking_id, token)

    # Assert
    get_booking_request = booking_api.get_booking(booking_id)

    assert delete_request.status_code == 201 and get_booking_request.status_code == 404

def test_delete_non_existed_booking_failed():
    # Arrange
    token_request = booking_api.auth(data.AUTH_BOOKING_BODY)

    # Достаем данные из ответа сервера
    token = token_request.json()['token']

    # Act
    delete_request = booking_api.delete_booking(data.get_random_int(), token)

    # Assert
    assert delete_request.status_code == 405