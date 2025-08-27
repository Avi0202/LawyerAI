from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
qdrant = QdrantClient("localhost", port=6333)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

query = "Can my landlord evict me without notice in Delhi?"
vector = model.encode(query).tolist()

results = qdrant.search(
    collection_name="indian_law",
    query_vector=vector,
    limit=3
)

for r in results:
    print(r.payload["source"], "→", r.payload["text"][:120], "...")