from transformers import pipeline

# Load the summarization model (downloads once, ~1.6GB, be patient!)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text, max_len=130, min_len=30):
    # NewsAPI content is sometimes cut off, so we clean it
    if not text or len(text.split()) < 30:
        return "Not enough content to summarize."
    
    # BART has a token limit, so trim long texts
    text = text[:1024]
    
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]["summary_text"]


# ✅ Test it
if __name__ == "__main__":
    test_text = """
    Adobe has launched its new AI assistant, Firefly, which aims to assist creative 
    professionals perform tasks within Adobe's photo, video, and digital content editing 
    software. Firefly would be able to take instructions and autonomously use tools like 
    Photoshop to complete complex editing workflows. The assistant uses large language 
    models combined with Adobe's own creative AI to understand natural language commands 
    and execute multi-step editing tasks automatically.
    """
    
    print("Original Text:")
    print(test_text)
    print("\nAI Summary:")
    print(summarize(test_text))