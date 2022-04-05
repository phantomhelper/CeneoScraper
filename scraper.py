from importlib.resources import contents
from bs4 import BeautifulSoup
import requests
from translate import Translator
# translator= Translator(to_lang="German")
# translation = translator.translate("Good Morning!")
# print (translation)

url = "https://www.ceneo.pl/113706425#tab=reviews"

r = requests.get(url)

if r.status_code == 200:
    print('[INFO]: Roger.')

    soup = BeautifulSoup(r.text, 'html.parser')
    opinions = soup.find_all("div", class_="js_product-review")
    translator = Translator(to_lang="en")
    for opinion in opinions:
        # print(opinion)
        opinion_id = opinion.select("div")['data-entry-id']
        author = opinion.select("span.user-post__author-name").text.strip()
        rcmd = opinion.select("span.user-post__author-recomendation > em").strip()
        score = opinion.select("span.user-post__score-count").strip()
        content = opinion.select("div.user-post__text")
        pros = opinion.select("div.review-feature__title--positives ~ div.review-feature__title")
        cons = opinion.select("div.review-feature__title--positives ~ div.review-feature__title")
        posted_on = opinion.select("span.user-post__published > time:nth-child(1)")['datetime']
        bought_on = opinion.select("span.user-post__published > time:nth-child(2)")['datetime']
        usefull = opinion.select("button.js_vote-yes")
        useless = opinion.select("button.js_vote-no")

        pros = [item.text.strip() for item in pros]
        cons = [item.text.strip() for item in cons]







        # # Author name
        # author_name = opinion.find("span", "user-post__author-name").text
        # print(f"Author name: {author_name}")

        # # Text
        # text = opinion.find("div", 'user-post__text').text
        # text = translator.translate(text)
        # print(f"Content: \n{text}")

        # # Advantages
        # advantages = opinion.find_all("div", "review-feature__item")
        # if advantages:
        #     print("\nAdvantages:")
        #     for advantage in advantages:
        #         print(f" [+] {translator.translate(advantage.text)};")

        # # Disadvantages
        # disadvantages = opinion.find_all("div", "review-feature__title--negatives")
        # if disadvantages:
        #     print("\nDisadvantages:")
        #     for disadvantage in disadvantages:
        #         print(f" [+] {translator.translate(disadvantage.text)};")
        print("\n- "*10)
            

    


else:
    print(f"[INFO]: Something went wrong...\nStatus code: {r.status_code}")