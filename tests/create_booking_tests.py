import pytest

import booking_api
import data


# Given When Then
def test_create_booking_success():
    # Arrange
    # Act
    created_booking_request = booking_api.create_booking(data.CREATE_BOOKING_BODY)

    # Assert
    assert created_booking_request.status_code == 200 and created_booking_request.json()['bookingid'] > 0

@pytest.mark.parametrize("new_name", [
    pytest.param("O", id="Check 1 letter name"),
    pytest.param("Oleg", id="Check normal name"),
    pytest.param("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", id="Check big name")
])
def test_create_booking_with_custom_firstname_success(new_name):
    # Arrange
    # Act
    created_booking_request = booking_api.create_booking(data.modify_firstname_booking_body(new_name))

    # Assert
    assert (created_booking_request.status_code == 200 and
            created_booking_request.json()['booking']['firstname'] == new_name)