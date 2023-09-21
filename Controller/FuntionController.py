import os

import requests

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

  if message == "/image_mmi":
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

  if message == "/intensity_logo":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        url_imageMMIjpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}_rev/intensity_logo.jpg'
        return url_imageMMIjpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  if message == "/impact_list":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        url_imageMMIjpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}_rev/impact_list.jpg'
        return url_imageMMIjpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  if message == "/stationlist_MMI":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        url_imageMMIjpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}_rev/stationlist_MMI.jpg'
        return url_imageMMIjpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  if message == "/loc_map":
    url_new = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        url_imageMMIjpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}_rev/loc_map.png'
        return url_imageMMIjpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  return """Invalid command. Please use :
/new
/intensity_logo
/impact_list
/image_mmi
/stationlist_MMI
/loc_map"""


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
