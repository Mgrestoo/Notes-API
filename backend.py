from webbrowser import get
import requests

endpoint = 'https://en.surebet.com/surebets'

get_bets = requests.get(endpoint)
print(get_bets.status_code)
# print(get_bets.json())
print(get_bets.text)
