import os
from .preprocess import chunk_text
from .embed_store import store_chunks
from docx import Document

data_dir = os.path.join(os.path.dirname(__file__), "data")

def read_docx(path):
    """Extract text from a Word (.docx) file."""
    doc = Document(path)
    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():  # store non-empty paragraphs
            full_text.append(para.text.strip())
    return "\n".join(full_text)

for filename in os.listdir(data_dir):
    file_path = os.path.join(data_dir, filename)

    if filename.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif filename.endswith(".docx"):
        text = read_docx(file_path)

    else:
        print(f"⚠️ Skipping {filename} (unsupported format)")
        continue

    # Chunk + store into Qdrant
    chunks = chunk_text(text, max_length=500)  #list of chunks
    law_name = os.path.splitext(filename)[0]   # remove extension
    store_chunks(chunks, source=law_name)
    print(f"✅ Ingested '{law_name}' with {len(chunks)} chunks into Qdrant.")