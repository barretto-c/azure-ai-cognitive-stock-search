from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

endpoint = os.getenv("SEARCH_ENDPOINT")
key = os.getenv("SEARCH_ADMIN_KEY")
index_name = os.getenv("INDEX_NAME", "stocks")

search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

docs = [
    {
        "ticker": "AAPL",
        "company": "Apple Inc.",
        "sector": "Technology",
        "description": "Consumer electronics, iPhones, Macs, services, and AI investments",
        "marketCap": 3200000000000
    },
    {
        "ticker": "NVDA",
        "company": "NVIDIA Corporation",
        "sector": "Semiconductors",
        "description": "GPUs, AI accelerators, data center compute, and autonomous systems",
        "marketCap": 2500000000000
    },
    {
        "ticker": "TSLA",
        "company": "Tesla Inc.",
        "sector": "Automotive",
        "description": "Electric vehicles, robotics, and autonomous driving",
        "marketCap": 800000000000
    },
    {
        "ticker": "MSFT",
        "company": "Microsoft Corporation",
        "sector": "Technology",
        "description": "Cloud computing, enterprise software, and AI platforms",
        "marketCap": 3100000000000
    },
    {
        "ticker": "AMBY",
        "company": "Amighty By",
        "sector": "Fictional",
        "description": "Innovative AI-driven solutions and fictional stock for demo purposes",
        "marketCap": 1234567890
    },
    {
        "ticker": "OAI",
        "company": "OpenAI",
        "sector": "Artificial Intelligence",
        "description": "AI research, language models, and generative AI technologies",
        "marketCap": 500000000000
    },
]

result = search_client.upload_documents(docs)
print("Upload results:")
for r in result:
    print(f"Key: {r.key}, Succeeded: {r.succeeded}, Error: {r.error_message}")