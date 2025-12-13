from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

import os
from dotenv import load_dotenv
from textblob import TextBlob

load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# Load static data with recent news headlines for each stock
import json
static_data_path = os.path.join(os.path.dirname(__file__), "static_stock_data.json")
with open(static_data_path, "r", encoding="utf-8") as f:
    docs = json.load(f)


# For each stock, keep only 'news' (string) and compute/store 'newsSentiment' (double)
for doc in docs:
    # If 'news' is not present, use the first item from 'recentNews' if available
    news = doc.get('news')
    if not news:
        recent_news = doc.get('recentNews')
        if recent_news and isinstance(recent_news, list) and len(recent_news) > 0:
            news = recent_news[0]
        else:
            news = ''
    doc['news'] = news
    # Compute sentiment for the news string
    doc['newsSentiment'] = round(TextBlob(news).sentiment.polarity, 3) if news else None
    # Remove any other news/recentNews fields
    doc.pop('recentNews', None)
    doc.pop('recentNewsSentiments', None)
endpoint = os.getenv("SEARCH_ENDPOINT")
key = os.getenv("SEARCH_ADMIN_KEY")
index_name = os.getenv("INDEX_NAME", "stocks")

search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))


result = search_client.upload_documents(docs)
print("Upload results:")
for r in result:
    print(f"Key: {r.key}, Succeeded: {r.succeeded}, Error: {r.error_message}")