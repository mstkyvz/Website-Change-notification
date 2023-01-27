import requests
import time
import urllib
# Telegram Bot API token

TOKEN = 'TOKEN'

# Telegram kullanıcı ID
CHAT_ID = 'CHAT_ID'

# Kontrol etmek istediğiniz web sayfasının URL'si
URL = 'https://www.example.com/'

# İlk çekim için içeriği kaydedin
first_content = requests.get(URL).text

while True:
    current_content = requests.get(URL).text
    soup = BeautifulSoup(current_content, 'html.parser')
    navlist = soup.select('.navlist') # = soup.find_all("div", attrs={"class":"DetailsArea_L"}) kullanabilirsiniz değişiklik gösteriyor
    if current_content != first_content or (navlist and navlist != first_navlist):
        params = {
            'chat_id': CHAT_ID,
            'text': "Web sayfasında değişiklikler tespit edildi! " + URL
        }
        bot_url = f'https://api.telegram.org/bot%7BTOKEN%7D/sendMessage?'
        params_encoded = urllib.parse.urlencode(params)
        requests.get(bot_url + params_encoded)
        first_content = current_content
        first_navlist = navlist
    time.sleep(15)
