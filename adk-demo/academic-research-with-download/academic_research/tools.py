import requests
import os
from pathlib import Path
import uuid
import fitz  # PyMuPDF

def download_pdf(url: str):
    """Downloads a PDF from a URL, saves it, and returns its content.

    Args:
        url: The URL of the PDF to download.

    Returns:
        A dictionary containing the path and content of the PDF, or None on failure.
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Get filename from URL or generate a unique one
        filename = url.split('/')[-1]
        if not filename or not filename.lower().endswith('.pdf'):
            filename = f"{uuid.uuid4()}.pdf"

        # Get the download path
        download_dir = Path.home() / "Downloads"
        
        # Ensure the directory exists
        download_dir.mkdir(parents=True, exist_ok=True)
        
        file_path = download_dir / filename

        # Write the content of the response to the file
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()

        return {"file_path": str(file_path), "pdf_content": text}
    except requests.RequestException as e:
        print(f"Failed to download PDF from {url}: {str(e)}")
        return None
    except Exception as e:
        print(f"Failed to parse PDF from {url}: {str(e)}")
        return None
