
from pathlib import Path
import chromadb


DB_PATH = "chroma_db"
COLLECTION_NAME = "enterprise_documents"


def get_collection():
    Path(DB_PATH).mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"}
    )

    return collection


def store_embeddings(chunks: list[dict], embeddings):
    collection = get_collection()

    ids = [
        f"{chunk['source']}-p{chunk['page']}-c{chunk['chunk_id']}"
        for chunk in chunks
    ]

    documents = [chunk["text"] for chunk in chunks]

    metadatas = [
        {
            "source": chunk["source"],
            "page": chunk["page"],
            "chunk_id": chunk["chunk_id"]
        }
        for chunk in chunks
    ]

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    return collection
