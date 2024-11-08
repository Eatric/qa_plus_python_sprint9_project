import random

CREATE_BOOKING_BODY = {
    "firstname" : "Kamil",
    "lastname" : "Brown",
    "totalprice" : 1110,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

AUTH_BOOKING_BODY = {
    "username" : "admin",
    "password" : "password123"
}

def modify_firstname_booking_body(value):
    return modify_create_booking_body("firstname", value)

def modify_create_booking_body(key, value):
    body = CREATE_BOOKING_BODY.copy()
    body[key] = value

    return body

def get_random_int():
    return random.randint(1000000000, 2000000000)
