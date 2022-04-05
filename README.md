# CeneoScraper

## Single  opinion structure

|Element|Selector|Variable|
|---|---|---|
|Opinion|div.js_product-review|opinion|
|Opinion ID|div\["data-entry-id"\]|opinion_id|
|Author|span.user-post__author-name|author|
|Recommendation|span.user-post__author-recomendation- > em| rcmd |
|Stars score|span.user-post__score-count|score|
|Content|div.user-post__text|content|
|List of advantages|div.review-feature__title--positives ~ div.review-feature__title|pros|
|List of disadvantages|div.review-feature__title--negatives ~ div.review-feature__title|cons|
|Date of posting opinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\] |bought_on|
|For how many users usefull|button.js_vote-yes > span|usefull|
|For how many users useless|button.js_vote-no > span|useless|