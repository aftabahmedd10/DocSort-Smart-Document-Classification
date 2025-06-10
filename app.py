import streamlit as st
from PIL import Image
import pdfplumber
import tempfile
from src import process_image, process_pdf


# App Title
st.set_page_config(page_title="DocSort - Smart Document Classifier", layout="centered")

# Header
st.title("📄 DocSort: Smart Document Classification")
st.markdown("""
Welcome to **DocSort** – your intelligent assistant to automatically **classify documents** such as **invoices, contracts, receipts**.  
Upload a document, and let our AI model sort it for you in seconds!

---

### 📤 Upload your Document
You can upload **PDF**, **JPG**, or **PNG** files.
""")

# File uploader
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "jpg", "jpeg", "png"])

# Function to display file
def display_file(file):
    file_type = file.type
    if "image" in file_type:
        image = Image.open(file).resize((500, 300))
        st.image(image, caption="Uploaded Document", use_container_width=False)
    elif file_type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.read())
            with pdfplumber.open(tmp_file.name) as pdf:
                page = pdf.pages[0]
                st.image(page.to_image(resolution=80).original, caption="First Page of PDF", use_container_width=False)

# When file is uploaded
if uploaded_file:
    display_file(uploaded_file)

    file_type = uploaded_file.type

    st.markdown("---")
    st.markdown("### 🧠 Classifying Document...")
    
    # Placeholder for your classification logic
    with st.spinner("Analyzing document..."):
        classification_result = None
        
        if "image" in file_type:
            classification_result = process_image.process(uploaded_file).strip()

        elif file_type == "application/pdf":
            classification_result = process_pdf.process(uploaded_file).strip()


    st.success(f"✅ Document Classified as: **{classification_result}**")

    st.markdown("Feel free to upload another document or explore the results.")
    st.balloons()
else:
    st.info("Please upload a document to get started.")

# Footer
st.markdown("---")
st.caption("🔐 Your files are processed securely and never stored.")
st.caption("Made with ❤️ using Streamlit and AI")
