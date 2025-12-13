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

# Get all document keys (assuming 'ticker' is the key field)
results = search_client.search("*", select=["ticker"], top=1000)
doc_keys = [doc["ticker"] for doc in results]

if not doc_keys:
    print("No documents found to delete.")
else:
    actions = [{"@search.action": "delete", "ticker": key} for key in doc_keys]
    result = search_client.upload_documents(actions)
    print("Delete results:")
    for r in result:
        print(f"Key: {r.key}, Succeeded: {r.succeeded}, Error: {r.error_message}")
