from textblob import TextBlob

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given string of text.
    Returns a polarity score between -1.0 (negative) and 1.0 (positive).
    """
    analysis = TextBlob(text)
    # Polarity is the numerical sentiment score
    return analysis.sentiment.polarity

if __name__ == "__main__":
    # Test with a sample headline
    headline = "Bitcoin price surges as major adoption news breaks"
    score = analyze_sentiment(headline)
    print(f"Headline: {headline}")
    print(f"Sentiment Score: {score}")
