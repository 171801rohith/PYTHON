# Use the NewsAPI and the requests module to fetch the daily news related to different topics.
# Go to: https://newsapi.org/ and explore the various options to build you application.

import requests
import json

query = input("What type of news you are interested in : ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-03&sortBy=publishedAt&apiKey=apii"
r = requests.get(url)
news = json.loads(r.text)
print(news, type(news))

with open(
    "C:\\Users\\rohit\\Desktop\\PYTHON\\OS Example\\Tutorial1\\news.json", "w"
) as f:
    json.dump(news, f, indent=4)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-" * 169)