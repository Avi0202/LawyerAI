import uuid
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct,VectorParams
from sentence_transformers import SentenceTransformer
import os

# Connect Qdrant
qdrant = QdrantClient(host="localhost", port=6333)

qdrant.recreate_collection(
    collection_name="indian_law",
    vectors_config=VectorParams(size=384, distance="Cosine")
)
# Embeddings model 
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def store_chunks(chunks, source="unknown", collection_name="indian_law"):
    vectors = embedding_model.encode(chunks).tolist()

    points = []
    for chunk, vector in zip(chunks, vectors):
        points.append(PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={"text": chunk, "source": source}
        ))

    qdrant.upsert(collection_name=collection_name, points=points)
    print(f"✅ Stored {len(points)} chunks from {source}")