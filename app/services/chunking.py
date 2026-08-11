def fixed_chunking(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> list[str]:
    """
    Split text into fixed-size chunks with overlap.
    """

    chunks = []

    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]

        if chunk:
            chunks.append(chunk)

    return chunks