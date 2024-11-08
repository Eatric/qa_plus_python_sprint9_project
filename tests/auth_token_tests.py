import booking_api
import data


def test_auth_token_success():
    # Act
    auth_token_request = booking_api.auth(data.AUTH_BOOKING_BODY)

    # Assert
    assert auth_token_request.status_code == 200