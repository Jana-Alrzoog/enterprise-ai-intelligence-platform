
from src.ingestion.embedder import load_embedding_model
from src.retrieval.retriever import retrieve


model = load_embedding_model()

query = "What was the company's total revenue in 2025?"

results = retrieve(query, model, top_k=3)

print(f"\nQuery: {query}")
print(f"Retrieved chunks: {len(results)}")

for i, result in enumerate(results, start=1):
    print(f"\n--- Result {i} ---")
    print(f"Source: {result['source']}")
    print(f"Page: {result['page']}")
    print(f"Cosine distance: {result['distance']:.4f}")
    print(f"Text:\n{result['text'][:500]}")
