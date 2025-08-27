from .deps import qdrant, embed_text, generate_answer

COLLECTION_NAME = "indian_law"

def retrieve_relevant_passages(query: str, top_k=3):
    query_vector = embed_text(query)
    results = qdrant.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=top_k
    )
    passages = [hit.payload["text"] for hit in results]
    return passages

def rag_pipeline(query: str):
    context_passages = retrieve_relevant_passages(query)
    context = "\n".join(context_passages)
    answer = generate_answer(query, context)
    return answer, context_passages