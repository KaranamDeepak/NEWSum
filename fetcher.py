import requests

API_KEY = "7200c78b976b42aa88bbef5537d1eff4 "

def fetch_news(topic, count=5):
    url = f"https://newsapi.org/v2/everything?q={topic}&pageSize={count}&apiKey={API_KEY}&language=en&sortBy=publishedAt"
    
    response = requests.get(url)
    data = response.json()

    articles = []

    for article in data["articles"]:
        articles.append({
            "title": article["title"],
            "description": article["description"],
            "content": article["content"],
            "url": article["url"],
            "source": article["source"]["name"]
        })

    return articles


# ✅ Test it
if __name__ == "__main__":
    results = fetch_news("artificial intelligence")
    for i, article in enumerate(results):
        print(f"\n--- Article {i+1} ---")
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']}")
        print(f"Description: {article['description']}")