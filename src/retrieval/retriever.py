
from src.ingestion.embedder import generate_embeddings
from src.retrieval.vector_store import get_collection


def retrieve(query: str, model, top_k: int = 3):
    collection = get_collection()

    if collection.count() == 0:
        return []

    query_embedding = generate_embeddings([query], model)[0]

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"]
    )

    retrieved_chunks = []

    for text, metadata, distance in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0]
    ):
        retrieved_chunks.append({
            "text": text,
            "source": metadata["source"],
            "page": metadata["page"],
            "distance": distance
        })

    return retrieved_chunks
