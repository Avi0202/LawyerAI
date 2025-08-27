def chunk_text(text: str, max_length: int = 500):
    words = text.split()
    chunks, current = [], []
    for word in words:
        if len(" ".join(current + [word])) > max_length:
            chunks.append(" ".join(current))
            current = [word]
        else:
            current.append(word)
    if current:
        chunks.append(" ".join(current))
    return chunks