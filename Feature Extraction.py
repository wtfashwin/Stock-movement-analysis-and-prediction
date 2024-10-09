# Feature Extraction: Extract features like sentiment polarity and frequency of mentions

df['title_sentiment'] = df['cleaned_title'].apply(get_sentiment)
df['selftext_sentiment'] = df['cleaned_selftext'].apply(get_sentiment)
# Additional feature extraction, such as frequency of mentions, can be added here
