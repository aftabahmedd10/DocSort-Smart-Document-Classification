# DocuSort

**DocuSort** is a document classification and extraction tool designed to help users upload documents (PDF, JPG, PNG), automatically identify the document type, and extract relevant text data. The system provides a user-friendly interface for uploading files, viewing classification results with confidence scores, and exporting the extracted data.

---

## Features

- Upload documents via drag-and-drop or file selection
- Automatic document type classification with confidence scores
- Text extraction from uploaded documents
- Export extracted data
- Minimalistic UI with easy navigation

---

## Technologies Used

- Python
- Flask (Backend API)
- Tesseract OCR (for text extraction)
- scikit-learn (for document classification)
- Streamlit (for frontend interface)
- HTML/CSS/JavaScript (UI components)

---

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

---

## Setup Instructions

### 1. Clone the repository

### 2. Create virtual enviornment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Tesseract OCR

- Windows:

Download the installer from Tesseract OCR
Run the installer and follow instructions
Add Tesseract to your system PATH

- Linux:
```bash
sudo apt-get install tesseract-ocr
```

-MacOS
```bash
brew install tesseract
```

### 5. Run Streamlit app
```bash
streamlit run app.py
```

### Usage
1. Launch the app with the command above.
2. Upload a document (PDF, JPG, PNG).
3. View the classification result with confidence score.
4. View the extracted text.
5. Export the data if needed.

