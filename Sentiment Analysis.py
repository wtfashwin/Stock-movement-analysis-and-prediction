from textblob import TextBlob
import pandas as pd

# Sentiment Analysis: Apply sentiment analysis to the cleaned data
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Apply to DataFrame
df = pd.DataFrame(data)
df['cleaned_title'] = df['title'].apply(clean_text)
df['cleaned_selftext'] = df['selftext'].apply(clean_text)
df['title_sentiment'] = df['cleaned_title'].apply(get_sentiment)
df['selftext_sentiment'] = df['cleaned_selftext'].apply(get_sentiment)
