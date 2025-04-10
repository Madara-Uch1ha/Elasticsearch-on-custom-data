import os
import glob
# import markdown  # Optional: for converting markdown to HTML
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

# Connect to Elasticsearch (assumes running on localhost:9200)
es = Elasticsearch("http://localhost:9200",
                   basic_auth=(os.getenv('username'),os.getenv('password')))  # Replace with your credentials

def create_index(index_name):
    # Check if the index already exists
    if es.indices.exists(index=index_name):
        print(f"Index '{index_name}' already exists.")
    else:
        mapping = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "properties": {
                    "filename": {"type": "text"},
                    "content": {"type": "text"}
                }
            }
        }
        es.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' created.")

def index_markdown_files(data_folder, index_name):
    # Look for all .md files in the specified folder
    md_files = glob.glob(os.path.join(data_folder, "*.md"))
    if not md_files:
        print("No markdown files found.")
        return

    for md_file in md_files:
        with open(md_file, "r", encoding="utf8") as f:
            content = f.read()

            # Optional: convert markdown to HTML if needed
            # html_content = markdown.markdown(content)

            doc = {
                "filename": os.path.basename(md_file),
                "content": content  # or "content": html_content if using HTML conversion
            }
            response = es.index(index=index_name, document=doc)
            print(f"Indexed {md_file} with ID: {response['_id']}")

if __name__ == "__main__":
    index_name = "md-files"
    data_folder = os.path.join(os.getcwd(), "data")  # Adjust if your extracted folder has a different path
    create_index(index_name)
    index_markdown_files(data_folder, index_name)
