import requests
import configuration
import data

def create_user():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=data.user_body)

def get_token():
    token_body = create_user().json()
    return token_body["authToken"]
    # или другой вариант return create_toke().json()["authToken"]


def create_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=body,
                         headers={"Authorization": "Bearer " + get_token()})

