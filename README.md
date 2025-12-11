
# azure-ai-cognitive-stock-search
A fully serverless, Azure-powered AI search engine for stock data, deployed under the AmightyByte brand at https://amightybyte.com/stocks.

## Quick Start

### 1. Set Up Python Environment
- Create a virtual environment:
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

### 2. Install Dependencies
```bash
pip install -r requirements.txt
pip install python-dotenv requests
```

### 3. Provision Azure Search Service
- Create your Azure Cognitive Search service:
   ```bash
   az search service create --name <your_resource_name> --resource-group <your_resource_group> --sku free --location eastus
   ```

### 4. Configure Credentials
- In the Azure portal or via CLI, find your:
   - SEARCH_ENDPOINT
   - SEARCH_ADMIN_KEY
- Add these to a `.env` file in your project root:
   ```env
   SEARCH_ENDPOINT=<your-endpoint>
   SEARCH_ADMIN_KEY=<your-admin-key>
   INDEX_NAME=stocks
   ```

### 5. Create the Search Index
- Run:
   ```bash
   python search/create_index.py
   ```

### 6. Upload Documents
- Run:
   ```bash
   python search/upload_docs.py
   ```

### 7. Verify in Azure Portal
- Go to your Azure Search resource in the portal and check that the index and documents are present.

---

For advanced queries, use curl or the Azure Portal's Search Explorer. See script files for customization.
