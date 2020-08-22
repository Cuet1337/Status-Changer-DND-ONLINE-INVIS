import os
import random
import requests
from colorama import Fore
import os

token = 'TOKEN-HERE'
# Dont use on main or ur account will be banned LOL


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
payload = {
    'status': "online",
  }
payload2 = {
    'status': "dnd",
  }
payloadd3 = {
  'status': "invisible"
}
while True:
  request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
  request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload2)
  request.patch("https://discordapp.com/api/v6/users/@me/settings",headers=headers, json=payloadd3)
