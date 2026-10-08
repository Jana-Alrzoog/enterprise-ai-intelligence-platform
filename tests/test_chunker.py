
from src.ingestion.pdf_loader import load_pdf
from src.ingestion.chunker import chunk_documents

documents = load_pdf("data/sample.pdf")
chunks = chunk_documents(documents)

print(f"Extracted pages: {len(documents)}")
print(f"Total chunks: {len(chunks)}")

for chunk in chunks[:3]:
    print("\n--------------------")
    print(f"Source: {chunk['source']}")
    print(f"Page: {chunk['page']}")
    print(f"Chunk ID: {chunk['chunk_id']}")
    print(f"Length: {len(chunk['text'])}")
    print(f"Text: {chunk['text'][:200]}")
