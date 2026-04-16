from textblob import TextBlob

def analyze_sentiment(text):
    if not text:
        return "Neutral"
    
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    # polarity is between -1 (very negative) to +1 (very positive)

    if polarity > 0.1:
        return f"🟢 Positive (score: {round(polarity, 2)})"
    elif polarity < -0.1:
        return f"🔴 Negative (score: {round(polarity, 2)})"
    else:
        return f"🟡 Neutral (score: {round(polarity, 2)})"


# ✅ Test it
if __name__ == "__main__":
    test_articles = [
        "The stock market surged today with amazing gains and incredible growth!",
        "The company collapsed and filed for bankruptcy amid massive losses.",
        "The government released a new report on infrastructure spending today."
    ]

    for article in test_articles:
        print(f"Text: {article}")
        print(f"Sentiment: {analyze_sentiment(article)}")
        print()