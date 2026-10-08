
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import chunk_documents
from src.ingestion.embedder import (
    load_embedding_model,
    generate_embeddings
)
from src.retrieval.vector_store import store_embeddings


documents = load_pdf("data/sample.pdf")
chunks = chunk_documents(documents)

model = load_embedding_model()
embeddings = generate_embeddings(
    [chunk["text"] for chunk in chunks],
    model
)

collection = store_embeddings(chunks, embeddings)

print(f"Stored chunks: {collection.count()}")
