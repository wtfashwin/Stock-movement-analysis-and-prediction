# Stock Movement Analysis and Prediction

Early Python experiments for collecting Reddit stock discussions and exploring their sentiment.

## What is included

- An asyncpraw collector for titles, scores, and post text.
- Text cleaning for URLs, mentions, hashtags, and numbers.
- TextBlob sentiment polarity calculations.
- pandas feature snippets and a Matplotlib/Seaborn sentiment chart.

## Status

Disconnected prototype scripts. There is no complete pipeline, stock-price dataset, trained prediction model, or evaluated forecast in the repository. The project name describes the intended direction; the captured source covers sentiment-analysis pieces.

## Before running

The collector needs your own Reddit API access. `Data Processing.py` currently embeds credential configuration; replace it with your own local environment-based configuration before making requests. Never reuse or republish an embedded secret.

The source imports asyncpraw, nest_asyncio, pandas, TextBlob, Matplotlib, and Seaborn. `requirements.txt` contains Markdown code-fence text, so it must be repaired before it can serve as a pip requirements file.

There is no supported one-command run. The scripts also need connecting:

- `Sentiment Analysis.py` expects `data` and `clean_text` from other files without importing them.
- `Feature Extraction.py` and `Visualization.py` expect an existing DataFrame and functions.
- `Data Processing.py` places `await main()` inside `main()` and has no top-level invocation.

Once these gaps are resolved, the intended workflow is to collect Reddit posts, clean the text, calculate polarity, and inspect the chart. It has not been verified as a working workflow.

## Source guide

- `Data Processing.py` — Reddit collector.
- `Data Preprocessing.py` — text cleaning.
- `Sentiment Analysis.py` — polarity and DataFrame snippets.
- `Feature Extraction.py` — sentiment feature snippets.
- `Visualization.py` — chart code.

## Checks and next steps

There is no automated test suite. More social platforms, stronger sentiment models, and external stock-price data remain future work. No relationship between sentiment and future market returns has been demonstrated here.

## License

No license file is included.
