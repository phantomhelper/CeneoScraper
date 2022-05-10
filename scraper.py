import json
import requests
from translate import Translator
from turtle import pos
from typing import Type
from bs4 import BeautifulSoup


def get_element(parrent, selector, attribute=None, return_list=False):
    try:
        if return_list:
            return [item.text.strip() for item in parrent.select(selector)]
        if attribute:
            return parrent.select_one(selector)[attribute]
        else:
            return parrent.select_one(selector).text.strip()
    except (AttributeError, TypeError):
        return None


to_lang = 'en'
from_lang = 'pl'
translator = Translator(to_lang=to_lang,from_lang=from_lang)
product_id = input('Please enter a product\'s id: ')

url = f"https://www.ceneo.pl/{product_id}#tab=reviews"

opinion_elements = {
    "author":  ["span.user-post__author-name"],
    "rcmd":  ["span.user-post__author-recomendation > em"],
    "score": ["span.user-post__score-count"],
    "content":  ["div.user-post__text"],
    "pros":  ["div.review-feature__title--positives ~ div.review-feature__item", None, True],
    "cons":  ["div.review-feature__title--negatives ~ div.review-feature__item", None, True],
    "posted_on":  ["span.user-post__published > time:nth-child(1)", "datetime"],
    "bought_on":  ["span.user-post__published > time:nth-child(2)", "datetime"],
    "usefull":  ["button.vote-yes > span"],
    "useless":  ["button.vote-no > span"],
}

all_opinions = []
while (url):
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, "html.parser")
    opinions = page_dom.select("div.js_product-review")

    for opinion in opinions:
        single_opinion = {
            key: get_element(opinion, *values)
            for key, values in opinion_elements.items()
        }
        single_opinion["opinion_id"] = opinion["data-entry-id"]
        single_opinion["rcmd"] = True if single_opinion['rcmd'] == "Polecam" else False if single_opinion['rcmd']=="Nie polecam" else None
        single_opinion["score"] = float(single_opinion["score"].split("/")[0].replace(",","."))
        single_opinion["usefull"] = int(single_opinion["usefull"])
        single_opinion["useless"] = int(single_opinion["useless"])
        single_opinion["content_en"] = translator.translate(single_opinion['content'])

        all_opinions.append(single_opinion)
        try:
            url = "https://www.ceneo.pl" + \
                get_element(page_dom, "a.pagination__next", "href")
        except TypeError:
            url = None

with open(f"opinions/{product_id}.json", "w", encoding="UTF-8") as f:
    json.dump(all_opinions, f, indent=4, ensure_ascii=False)
