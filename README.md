
# azure-ai-cognitive-stock-search
A fully serverless, Azure-powered AI search engine for stock data, deployed under the AmightyByte brand at https://amightybyte.com/stocks.

## Quick Start

### 1. Provision Azure Search Service
- Free (F1) tier (no semantic search):
  ```bash
  az search service create --name <your_resource_name> --resource-group <your_resource_group> --sku free --location eastus
  ```
- For semantic search, use S1 or higher (costs $100+/month):
  ```bash
  az search service create --name <your_resource_name> --resource-group <your_resource_group> --sku standard --location eastus
  ```

### 2. Set Up Python Environment
- Windows:
  ```cmd
  python -m venv .venv
  .\.venv\Scripts\activate.bat
  ```
- Linux/macOS:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install python-dotenv requests
```

### 4. Configure Credentials
- In the Azure portal or CLI, find:
  - SEARCH_ENDPOINT
  - SEARCH_ADMIN_KEY
- Add to `.env` in project root:
  ```env
  SEARCH_ENDPOINT=<your-endpoint>
  SEARCH_ADMIN_KEY=<your-admin-key>
  INDEX_NAME=stocks
  ```

### 5. Create the Search Index
```bash
python search/create_index.py
```

### 6. Upload Documents
```bash
python search/upload_docs.py
```

### 7. Verify in Azure Portal
- Check your Azure Search resource for the index and documents.

## Querying the Index (Search Examples)

**Keyword Search:**
curl -X POST "https://<service-name>.search.windows.net/indexes/<index-name>/docs/search?api-version=2023-11-01" -H "Content-Type: application/json" -H "api-key: <YOUR-ADMIN-KEY>" -d '{"search": "apple", "top": 5}'
**Vector Search:**
curl -X POST "https://<service-name>.search.windows.net/indexes/<index-name>/docs/search?api-version=2023-11-01" -H "Content-Type: application/json" -H "api-key: <YOUR-ADMIN-KEY>" -d '{"vector": {"value": [0.1, 0.2, ...], "fields": ["description"]}, "top": 5}'

**Hybrid Search (Keyword + Vector):**
curl -X POST "https://<service-name>.search.windows.net/indexes/<index-name>/docs/search?api-version=2023-11-01" -H "Content-Type: application/json" -H "api-key: <YOUR-ADMIN-KEY>" -d '{"search": "ai", "vector": {"value": [0.1, 0.2, ...], "fields": ["description"]}, "top": 5}'

Replace `<service-name>`, `<index-name>`, `<YOUR-ADMIN-KEY>`, and vector values as needed.

For advanced queries, use curl or the Azure Portal's Search Explorer. See script files for customization.