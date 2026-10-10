
from ollama import chat

MODEL_NAME = "qwen2.5:3b"


def generate_answer(question: str, context: str) -> str:
    response = chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
"content": (
    "You are an enterprise document intelligence assistant. "
    "Answer questions using ONLY the provided context. "
    "Every factual claim must include a citation in the format "
    "[Source N], where N refers to a source in the context. "
    "Only cite sources that directly support your answer. "
    "Never invent citations or information. "
    "If the answer is not supported by the context, respond exactly: "
    "I couldn't find that information in the provided documents."
),"content": (
    "You are an enterprise document intelligence assistant. "
    "Answer questions using ONLY the provided context. "
    "Every factual claim must include a citation in the format "
    "[Source N], where N refers to a source in the context. "
    "Only cite sources that directly support your answer. "
    "Never invent citations or information. "
    "If the answer is not supported by the context, respond exactly: "
    "I couldn't find that information in the provided documents."
),
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {question}",
            },
        ],
        options={"temperature": 0},
    )

    return response.message.content
