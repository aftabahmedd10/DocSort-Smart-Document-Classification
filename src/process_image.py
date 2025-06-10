from PIL import Image
from .document_classifier import classify_text

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def process(file):
    image = Image.open(file) 
    text = pytesseract.image_to_string(image)
    classification_result = classify_text(text)
    return classification_result


#print(read_pdf(img))




