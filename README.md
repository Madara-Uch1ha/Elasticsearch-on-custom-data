# Elasticsearch Markdown File Indexer

A Python script that indexes Markdown files into Elasticsearch for full-text search capabilities.

## Prerequisites

- Python 3.8+
- Elasticsearch 8.17.4
- Kibana 8.17.4
- Required Python packages:
  ```sh
  pip install -r requirements.txt
  ```

## Setup

1. Create a `.env` file in the project root with your Elasticsearch credentials:
   ```
   username=your_elasticsearch_username
   password=your_elasticsearch_password
   ```
   You can find them while running the server for the first time. More info look into Elasticsearch documentation.

2. Ensure Elasticsearch is running on `localhost:9200`

3. Place your Markdown files in the `data` directory

## Usage

Run the indexing script:
```sh
python index_md_files.py
```

The script will:
- Index all `.md` files from the `data` directory
- Store both filename and content for each file

## Searching Documents using Kibana

1. Open Kibana at `http://localhost:5601`

2. Go to Dev Tools > Console

3. Example queries:

Search all documents:
```
GET md-files/_search
```

Search for specific content:
```
GET md-files/_search
{
  "query": {
    "match": {
      "content": "your search term"
    }
  }
}
```

Search by filename:
```
GET md-files/_search
{
  "query": {
    "match": {
      "filename": "example.md"
    }
  }
}
```

## Index Structure

- `filename`: Name of the markdown file
- `content`: Raw content of the markdown file

## Note

Make sure both Elasticsearch and Kibana services are running before using the script or performing searches.

### Thank You :)
