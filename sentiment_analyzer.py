from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze sentiment of a given text."""
    if not text:
        return "neutral"
    
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score < 0:
        return "negative"
    elif sentiment_score > 0:
        return "positive"
    else:
        return "neutral"
