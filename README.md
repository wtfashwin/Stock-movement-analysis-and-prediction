# Stock Movement Analysis Based on Social Media Sentiment

This project analyzes and predicts stock movements by extracting and analyzing social media data, specifically from Reddit. It performs sentiment analysis on posts related to the stock market to provide insights into potential stock price trends. The project includes data collection from Reddit, preprocessing, sentiment analysis, and data visualization.

## Objective
- Scrape data from a specific subreddit that discusses stock market trends.
- Perform sentiment analysis on the scraped data.
- Visualize the correlations between sentiment and stock price movements.

## Features
- Data collection using `asyncpraw` from Reddit.
- Data preprocessing to clean text and prepare it for sentiment analysis.
- Sentiment analysis using `TextBlob` to gauge the mood of posts.
- Visualization of sentiment trends using `Matplotlib` and `Seaborn`.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/wtfashwin/stock-movement-analysis.git
   cd stock-movement-analysis-and-prediction


** Future Improvements
Extend data scraping to other social media platforms like Twitter and Telegram.
Improve the sentiment analysis by using more advanced techniques (e.g., VADER, BERT).
Correlate sentiment data with actual stock price movements using external APIs (e.g., Yahoo Finance).
