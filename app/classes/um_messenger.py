import bandwidth
from os import environ

def sendMessage(to, message):
    username = environ["UM_USERNAME"]
    token = environ["UM_TOKEN"]
    secret = environ["UM_SECRET"]
    number = environ["UM_NUMBER"]

    api = bandwidth.client('catapult', username, token, secret)
    message_id = api.send_message(from_ = number, to = to, text = message)
    return message_id
