from dotenv import load_dotenv
load_dotenv()

import os  # <- muta acest import imediat sub load_dotenv()

import chromadb
from chromadb.utils import embedding_functions

print("[DEBUG] OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))  # test linie

def get_chroma_collection():
    client = chromadb.Client(
        chromadb.config.Settings(
            persist_directory="./embeddings",
            anonymized_telemetry=False
        )
    )
    collection = client.get_or_create_collection(
        name="books",
        embedding_function=embedding_functions.OpenAIEmbeddingFunction(
            api_key=os.getenv("OPENAI_API_KEY"),
            model_name="text-embedding-3-small"
        )
    )
    return collection

def load_summaries(file_path: str) -> list[dict]:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    entries = content.strip().split("## Title:")
    docs = []
    for entry in entries:
        if entry.strip():
            lines = entry.strip().split("\n")
            title = lines[0].strip()
            summary = " ".join(line.strip() for line in lines[1:])
            docs.append({"title": title, "summary": summary})
    return docs

def populate_vectorstore():
    collection = get_chroma_collection()
    docs = load_summaries("data/book_summaries.txt")

    for idx, doc in enumerate(docs):
        collection.add(
            documents=[doc["summary"]],
            metadatas=[{"title": doc["title"]}],
            ids=[f"book_{idx}"]
        )

    print(f"Incarcat {len(docs)} rezumate in ChromaDB.")

def semantic_search(query: str, top_k: int = 3):
    collection = get_chroma_collection()
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results

if __name__ == "__main__":
    populate_vectorstore()

