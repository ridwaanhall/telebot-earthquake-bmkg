import os

import requests

import html2text

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

  elif message == "/narasi":
    url_new_1 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_1)
    narasi_url = 'https://bmkg-content-inatews.storage.googleapis.com/20230921110712_narasi.txt'
    response = requests.get(narasi_url)

    if response.status_code == 200:
      html_content = response.text
      plain_text_content = html2text.html2text(html_content)
      return plain_text_content
    else:
      return {"error": "Unable to fetch data from the URL."}

    #============================
    
    url_new_1 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_1)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        mmi_jpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}.mmi.jpg'
        print("mmi jpg",mmi_jpg)
        return mmi_jpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  elif message == "/image_mmi":
    url_new_1 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_1)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      if eventid is not None:
        mmi_jpg = f'https://earthquake-bmkg-api.ridwaanhall.repl.co/{eventid}.mmi.jpg'
        print("mmi jpg",mmi_jpg)
        return mmi_jpg
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  elif message == "/intensity_logo":
    url_new_2 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_2)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      print('Event ID',eventid)
      if eventid is not None:
        url_intensity_logo = f'https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/intensity_logo.jpg'
        print('Generated URL:', url_intensity_logo)
        return url_intensity_logo
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  elif message == "/impact_list":
    url_new_3 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_3)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      print('Event ID',eventid)
      if eventid is not None:
        url_impact_list = f'https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/impact_list.jpg'
        print('Generated URL:', url_impact_list)
        return url_impact_list
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  elif message == "/stationlist_MMI":
    url_new_4 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_4)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      print('Event ID',eventid)
      if eventid is not None:
        url_stationlist_MMI = f'https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/stationlist_MMI.jpg'
        print('Generated URL:', url_stationlist_MMI)
        return url_stationlist_MMI
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}

  elif message == "/loc_map":
    url_new_5 = 'https://earthquake-bmkg-api.ridwaanhall.repl.co/new.json'
    response = requests.get(url_new_5)

    if response.status_code == 200:
      info = response.json()["info"]
      eventid = info.get("eventid")
      print('Event ID',eventid)
      if eventid is not None:
        url_loc_map = f'https://bmkg-content-inatews.storage.googleapis.com/{eventid}_rev/loc_map.png'
        print('Generated URL:', url_loc_map)
        return url_loc_map
      else:
        return {"error": "No eventid found."}
    else:
      return {"error": "Unable to fetch data from the URL."}
  

  return """Invalid command. Please use :
/new
/image_mmi
/intensity_logo
/impact_list
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
