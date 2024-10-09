import matplotlib.pyplot as plt
import seaborn as sns

# Visualization: Plot sentiment analysis results
plt.figure(figsize=(12, 6))
sns.barplot(x='title', y='title_sentiment', data=df, palette='viridis')

plt.title('Sentiment Analysis of Titles')
plt.xlabel('Title')
plt.ylabel('Sentiment Score')

labels = [title.split()[0] for title in df['title']]
plt.xticks(range(len(labels)), labels, rotation=45, ha='right')
plt.tight_layout()
plt.show()
