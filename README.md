# NEWSum

NEWSum is a simple AI-powered news summarizer built with Streamlit.
It fetches the latest articles for a topic, generates short AI summaries, and shows sentiment analysis for each item.

## Features

- Fetches news articles from NewsAPI.org
- Summarizes article text using Hugging Face Transformers (`facebook/bart-large-cnn`)
- Analyzes article sentiment with TextBlob
- Displays results in a clean Streamlit interface

## Files

- `app.py` - Streamlit app layout and user interaction
- `fetcher.py` - NewsAPI fetch logic
- `summarizer.py` - AI text summarization logic
- `sentiment.py` - Sentiment scoring for article text

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add your NewsAPI key to `fetcher.py`:

```python
API_KEY = "YOUR_NEWSAPI_KEY"
```

3. Run the app:

```bash
streamlit run app.py
```

## Usage

- Enter a topic in the sidebar
- Choose how many articles to retrieve
- Click **Fetch News**
- View AI summaries and sentiment for each article

## Notes

- The summarization model downloads on first run and may take several minutes.
- If article text is too short, the app will display a message instead of summarizing.
