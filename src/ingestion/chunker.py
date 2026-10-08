
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents: list[dict]) -> list[dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )

    chunks = []

    for document in documents:
        texts = splitter.split_text(document["text"])

        for chunk_index, text in enumerate(texts):
            chunks.append({
                "text": text,
                "source": document["source"],
                "page": document["page"],
                "chunk_id": chunk_index
            })

    return chunks
