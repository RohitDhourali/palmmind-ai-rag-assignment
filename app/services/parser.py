from pathlib import Path
import pymupdf # PyMuPDF


def extract_text(file_path: Path) -> str:
    """
    Extract text from a PDF or TXT file.
    """

    extension = file_path.suffix.lower()

    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    elif extension == ".pdf":
        document = pymupdf.open(file_path)

        text = ""

        for page in document:
            text += page.get_text() + "\n"

        document.close()

        return text

    else:
        raise ValueError("Unsupported file type.")