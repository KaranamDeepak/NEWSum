import streamlit as st
from fetcher import fetch_news
from summarizer import summarize
from sentiment import analyze_sentiment

# --- Page Config ---
st.set_page_config(page_title="AI News Summarizer", page_icon="📰", layout="wide")

# --- Header ---
st.title("📰 AI-Powered News Summarizer")
st.markdown("Get real-time news with AI summaries and sentiment analysis")
st.divider()

# --- Sidebar ---
st.sidebar.header("🔍 Search Settings")
topic = st.sidebar.text_input("Enter a topic", value="artificial intelligence")
count = st.sidebar.slider("Number of articles", min_value=1, max_value=10, value=5)
search_btn = st.sidebar.button("🔎 Fetch News")

# --- Main Area ---
if search_btn:
    with st.spinner("Fetching news articles..."):
        articles = fetch_news(topic, count)

    if not articles:
        st.error("No articles found. Try a different topic!")
    else:
        st.success(f"Found {len(articles)} articles on **{topic}**")

        for i, article in enumerate(articles):
            st.subheader(f"📄 {article['title']}")
            st.caption(f"Source: {article['source']}")

            col1, col2 = st.columns(2)

            with col1:
                st.markdown("**📝 Original Description**")
                st.write(article["description"] or "No description available.")

            with col2:
                st.markdown("**🤖 AI Summary**")
                with st.spinner("Summarizing..."):
                    summary = summarize(article["description"] or "")
                st.write(summary)

            # Sentiment
            sentiment = analyze_sentiment(article["description"] or "")
            st.markdown(f"**Sentiment:** {sentiment}")
            st.markdown(f"[Read Full Article]({article['url']})")
            st.divider()

else:
    st.info("👈 Enter a topic in the sidebar and click Fetch News to get started!")