from PyPDF2 import PdfReader
import docx
import re

def extract_text(file_path):
    text = ""
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        for page in reader.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

def mask_email(text):
    return re.sub(r'[\w\.-]+@[\w\.-]+', '[email masked]', text)

def mask_name(text, name):
    return text.replace(name, '[Name masked]')
