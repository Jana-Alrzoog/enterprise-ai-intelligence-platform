
from src.ingestion.pdf_loader import load_pdf

documents = load_pdf("data/sample.pdf")

print(f"Total pages extracted: {len(documents)}")

for doc in documents[:2]:
    print(f"\nSource: {doc['source']}")
    print(f"Page: {doc['page']}")
    print(f"Text preview: {doc['text'][:300]}")
