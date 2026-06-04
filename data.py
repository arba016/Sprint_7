
BASE_URL = "https://qa-scooter.praktikum-services.ru"

CREATE_COURIER_URL = f"{BASE_URL}/api/v1/courier"
LOGIN_COURIER_URL = f"{BASE_URL}/api/v1/courier/login"
DELETE_COURIER_URL = f"{BASE_URL}/api/v1/courier"


CREATE_ORDER_URL = f"{BASE_URL}/api/v1/orders"

GET_ORDERS_URL = f"{BASE_URL}/api/v1/orders"


ORDER_GREY_SCOOTER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["GREY"],
}

ORDER_BLACK_SCOOTER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"],
}

ORDER_WITHOUT_COLOR_SCOOTER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
}

ORDER_BLACK_AND_GRAY_SCOOTER = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK", "GREY"],
}


WITHOUT_LOGIN = {
    "password": "1234",
    "firstName": "saske",
}

WITHOUT_PASSWORD = {
    "login": "ninja_without_password",
    "firstName": "saske",
}


RESPONSE_JSON_MESSAGE_OK = {"ok": True}
COURIER_REQUIRED_FIELDS_ERROR = "Недостаточно данных для создания учетной записи"
COURIER_ALREADY_EXISTS_ERROR = "Этот логин уже используется. Попробуйте другой."
COURIER_NOT_FOUND_ERROR = "Учетная запись не найдена"
LOGIN_REQUIRED_FIELDS_ERROR_MESSAGE = "Недостаточно данных для входа"

