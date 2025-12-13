import os
import requests
import json
from dotenv import load_dotenv
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

endpoint = os.getenv("SEARCH_ENDPOINT")
key = os.getenv("SEARCH_ADMIN_KEY")
index_name = os.getenv("INDEX_NAME", "stocks")

# REST API URL for index creation
api_version = "2023-11-01"
url = f"{endpoint}/indexes/{index_name}?api-version={api_version}"

# Index definition
index_definition = {
    "name": index_name,
    "fields": [
        {"name": "ticker", "type": "Edm.String", "key": True},
        {"name": "company", "type": "Edm.String", "searchable": True},
        {"name": "sector", "type": "Edm.String", "searchable": True},
        {"name": "description", "type": "Edm.String", "searchable": True},
        {"name": "marketCap", "type": "Edm.Int64"},
        {"name": "news", "type": "Edm.String", "searchable": True, "retrievable": True},
        {"name": "newsSentiment", "type": "Edm.Double", "retrievable": True}
    ],
    "semantic": {
        "configurations": [
            {
                "name": "default",
                "prioritizedFields": {
                    "titleField": {"fieldName": "company"},
                    "prioritizedContentFields": [
                        {"fieldName": "description"},
                        {"fieldName": "sector"}
                    ]
                }
            }
        ]
    }
}

headers = {
    "Content-Type": "application/json",
    "api-key": key
}

# Delete index if exists
delete_url = f"{endpoint}/indexes/{index_name}?api-version={api_version}"
requests.delete(delete_url, headers=headers)

# Create index
response = requests.put(url, headers=headers, data=json.dumps(index_definition))
if response.status_code == 201:
    print("Semantic Search Index created via REST API")
else:
    print(f"Failed to create index: {response.status_code}\n{response.text}")
