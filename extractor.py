import easyocr
import spacy
from pdfminer.high_level import extract_text
import re

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# OCR reader (for images)
reader = easyocr.Reader(['en'])

def extract_text_from_image(image):
    result = reader.readtext(image, detail=0)
    return ' '.join(result)

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_contact_entities(text):
    doc = nlp(text)
    name = email = phone = company = None

    # Extract email
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if match:
        email = match.group(0)

    # Extract phone number
    match = re.search(r'\+?\d[\d\s\-]{8,}\d', text)
    if match:
        phone = match.group(0)

    # Use SpaCy for name and organization
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not name:
            name = ent.text
        elif ent.label_ == "ORG" and not company:
            company = ent.text

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "company": company
    }
