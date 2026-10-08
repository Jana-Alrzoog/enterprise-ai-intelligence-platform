
from pathlib import Path
import pymupdf


def load_pdf(file_path: str) -> list[dict]:
    """
    Extract text from a PDF while preserving
    the source filename and page number.
    """

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"PDF not found: {path}")

    documents = []

    with pymupdf.open(path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text("text").strip()

            if not text:
                continue

            documents.append({
                "text": text,
                "source": path.name,
                "page": page_number
            })

    return documents
