from bs4 import BeautifulSoup
import requests


url = "https://www.ceneo.pl/45863470#tab=reviews"

r = requests.get(url)

if r.status_code == 200:
    print('[INFO]: Roger.')

    soup = BeautifulSoup(r.text, 'html.parser')
    # print(soup.prettify())
    opinions = soup.select("div.js_product-review")
    opinion=opinions.pop()
    print(type(opinion))
    


else:
    print(f"[INFO]: Something went wrong...\nStatus code: {r.status_code}")
