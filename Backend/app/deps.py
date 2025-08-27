from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv

import os


load_dotenv()
key=os.getenv("OPENAI_API_KEY")
# Qdrant connection
qdrant = QdrantClient("localhost", port=6333)

# Embeddings
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# LLM client (Gemini via OpenAI-compatible API)
client=OpenAI(
    api_key=key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def embed_text(text: str):
    return embedding_model.encode(text).tolist()

def generate_answer(query: str, context: str) -> str:
    prompt = f"""
                    You are a legal adviser specializing in Indian law.
                    Answer the following question using the information provided.

                    Question: {query}

                    {context}

                    Guidelines for your response:
                    - Do not mention or refer to 'context' or 'documents'.
                    - Provide a clear, authoritative legal analysis.
                    - Suggest possible legal interpretations or next steps.
                    - Cite relevant laws, sections, or case law where applicable.
                    - Do not say you are an AI system.
            """
    response = client.chat.completions.create(
        model="gemini-2.5-flash-lite",   
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content