import requests

import configuration


def auth(body):
    return requests.post(configuration.BASE_URL + configuration.AUTH_BOOKING_PATH, json=body)

def create_booking(body):
    return requests.post(configuration.BASE_URL + configuration.CREATE_BOOKING_PATH, json=body)

def delete_booking(booking_id: int, token):
    return requests.delete(configuration.BASE_URL + configuration.DELETE_BOOKING_PATH + str(booking_id), headers={
        'Cookie': 'token=' + token
    })

def get_booking(booking_id):
    return requests.get(configuration.BASE_URL + configuration.GET_BOOKING_PATH + str(booking_id))