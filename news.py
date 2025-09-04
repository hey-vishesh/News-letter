
import requests
API_KEY = "5827369fba5044bab7b0d78809489ab1"

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
    response = requests.get(url)
    articles = response.json().get("articles", [])

    headlines = []
    for article in articles[:5]:
        headlines.append(f"📰 {article['title']} ({article['source']['name']})")

    return "\n".join(headlines)
