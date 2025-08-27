Install all the dependencies 
pip install -r requirements.txt

**Step 1** Run Docker Engine
#for proto
docker run -p 6333:6333 qdrant/qdrant
#for persistence
docker run -p 6333:6333 -v ${PWD}/qdrant_storage:/qdrant/storage qdrant/qdrant 

**Step 2**
Check If Qdrant is working, run ingest/check_data.py and search_sample.py
If Vector db isn't working run "python -m ingest.load_data.py"
This will chunk,embed and store the data as vector in qdrant

**Step 3**
Add .env file in backend and store your api key under "OPENAI_API_KEY"

**Step 4**
start fasapi server from backend
uvicorn app.main:app --reload
#run UI proto
streamlit run UI_proto.py