import requests
import os

my_secret = os.environ['Bot_token']
chat_id = os.environ['chat_id']

def send_msg(text):
  requests.get(f'https://api.telegram.org/bot{my_secret}/sendMessage',
               params=dict(chat_id=chat_id,text=text))