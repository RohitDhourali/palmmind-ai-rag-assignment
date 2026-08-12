from langchain_text_splitters import RecursiveCharacterTextSplitter

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

    print(f"Total chunks created with fixed chunking: {len(chunks)}")
    return chunks


def recursive_chunking(
    text: str,
    chunk_size: int = 500,
    chunk_overlap: int = 50,
) -> list[str]:
    """
    Split text using recursive character chunking.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ],
    )
    chunks = splitter.split_text(text)
    print(f"Total chunks created with recursive chunking: {len(chunks)}")
    return chunks
