import nest_asyncio
import asyncio
import asyncpraw

# Allow nesting of asyncio event loops
nest_asyncio.apply()

# Data Collection: Code for scraping Reddit data
async def collect_data(subreddit_name, limit):
    async with asyncpraw.Reddit(client_id="VrFK4vKqvXXPEY7PsQBCQQ",
                               client_secret="u8gOMr0uFPGHoj7g1EJUs7aiTS5z3g",
                               user_agent="StockScraperApp") as reddit:

        subreddit = await reddit.subreddit(subreddit_name)
        posts = subreddit.new(limit=limit)

        data = {"title": [], "score": [], "selftext": []}

        async for post in posts:
            data["title"].append(post.title)
            data["score"].append(post.score)
            data["selftext"].append(post.selftext)

        return data

async def main():
    subreddit_name = "stocks"
    limit = 100
    data = await collect_data(subreddit_name, limit)
    print("Collected data:", data)

    await main()
