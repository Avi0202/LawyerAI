from qdrant_client import QdrantClient
qdrant = QdrantClient("localhost", port=6333)

print(qdrant.count("indian_law"))  