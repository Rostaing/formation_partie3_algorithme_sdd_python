import schedule
import time
import requests

# def dire_bonjour():
#     print("Salut, les amis de la data !")

# dire_bonjour()

# schedule.every(10).seconds.do(dire_bonjour)
# schedule.every(1).minutes.do(dire_bonjour)
# schedule.every(1).hour.do(dire_bonjour)
# schedule.every().monday.do(dire_bonjour)
# schedule.every().wednesday.do(dire_bonjour)
# schedule.every().day.at("12:27").do(dire_bonjour)
# schedule.every().minutes.at(":17").do(dire_bonjour)

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
page = requests.get(url)
data = page.json()

def fetch_bitcoin():
    print("Getting Bitcoin price...")
    result = data['bpi']['USD']
    print(result)

schedule.every(5).seconds.do(fetch_bitcoin)

while True:
    schedule.run_pending()
    time.sleep(1)