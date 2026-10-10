
from src.ingestion.embedder import load_embedding_model
from src.retrieval.retriever import retrieve
from src.generation.llm import generate_answer


def answer_question(question: str, model, top_k: int = 3):
    # Step 1: Retrieve relevant document chunks
    chunks = retrieve(question, model, top_k=top_k)

    if not chunks:
        return {
            "answer": "No documents were found.",
            "sources": []
        }

    # Step 2: Build context with source references
    context_parts = []

    for i, chunk in enumerate(chunks, start=1):
        context_parts.append(
            f"[Source {i}: {chunk['source']}, "
            f"Page {chunk['page']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    # Step 3: Generate an answer using the local LLM
    answer = generate_answer(question, context)

    # Step 4: Return the answer and retrieved sources
    sources = [
        {
            "file": chunk["source"],
            "page": chunk["page"],
            "distance": chunk["distance"]
        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "sources": sources
    }


if __name__ == "__main__":
    model = load_embedding_model()

    question = "What was Northstar Analytics' total revenue in 2025?"
    result = answer_question(question, model)

    print("\nQUESTION:")
    print(question)

    print("\nANSWER:")
    print(result["answer"])

    print("\nRETRIEVED SOURCES:")
    for source in result["sources"]:
        print(
            f"- {source['file']}, "
            f"Page {source['page']}, "
            f"Distance: {source['distance']:.4f}"
        )
