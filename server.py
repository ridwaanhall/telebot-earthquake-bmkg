import os

import requests
from flask import Flask, Response, request

app = Flask(__name__)
token = os.environ['TELEGRAM_BOT_TOKEN']


def generate_answer(message):
  if message == "/new":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      return info["headline"]
    else:
      return {"error": "Unable to fetch data from the URL."}

  if message == "/image_mmi_jpg":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        url_imageMMIjpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}.mmi.jpg'
        return url_imageMMIjpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  return "Invalid command. Please use '/new' or '/image_mmi_jpg'."


def message_parser(message):
  chat_id = message['message']['chat']['id']
  if 'text' in message['message']:
    text = message['message']['text']
    print("Chat ID: ", chat_id)
    print("Message: ", text)
    return chat_id, text
  else:
    print("Chat ID: ", chat_id)
    print("Message does not contain text.")
    return chat_id, "Message does not contain text."


def send_message_telegram(chat_id, text):
  url = f'https://api.telegram.org/bot{token}/sendMessage'
  payload = {'chat_id': chat_id, 'text': text}
  response = requests.post(url, json=payload)
  return response


def send_photo_telegram(chat_id, photo_url):
  url = f'https://api.telegram.org/bot{token}/sendPhoto'
  payload = {'chat_id': chat_id, 'photo': photo_url}
  response = requests.post(url, json=payload)
  return response


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    msg = request.get_json()
    chat_id, incoming_que = message_parser(msg)
    answer = generate_answer(incoming_que)

    if answer.startswith('http'):
      send_photo_telegram(chat_id, answer)
    else:
      send_message_telegram(chat_id, answer)
    return Response('ok', status=200)
  else:
    return "<h1>Something went wrong</h1>"
