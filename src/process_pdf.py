import pdfplumber
from .document_classifier import classify_text

def process(file):
    all_text = ""
    with pdfplumber.open(file) as pdf:
        for page_num, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                all_text += f"\n\n--- Page {page_num + 1} ---\n{text}"

    classification_result = classify_text(all_text)
    return classification_result