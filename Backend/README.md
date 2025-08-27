
#for proto
docker run -p 6333:6333 qdrant/qdrant
#for persistence
docker run -p 6333:6333 -v ${PWD}/qdrant_storage:/qdrant/storage qdrant/qdrant 

#start fasapi server from backend
uvicorn app.main:app --reload