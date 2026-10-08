
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import chunk_documents
from src.ingestion.embedder import (
    load_embedding_model,
    generate_embeddings
)


documents = load_pdf("data/sample.pdf")
chunks = chunk_documents(documents)

texts = [chunk["text"] for chunk in chunks]

model = load_embedding_model()
embeddings = generate_embeddings(texts, model)

print(f"Total chunks: {len(chunks)}")
print(f"Embeddings shape: {embeddings.shape}")
print(f"First vector preview: {embeddings[0][:10]}")
