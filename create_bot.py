import requests
import os

my_secret = os.environ['Bot_token']
user_id = 435133768
constantin_id = 408601450

def send_msg(text):
    token = my_secret
    chat_id = "435133768"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())