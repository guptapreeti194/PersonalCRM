import streamlit as st
from db import init_db, insert_contact, get_all_contacts
from extractor import extract_text_from_image, extract_text_from_pdf, extract_contact_entities
from linkedin import generate_linkedin_url, generate_connection_message
from utils import save_uploaded_file

# Vibrant Custom CSS
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ffecd2, #fcb69f);
        }
        .main {
            background-color: rgba(255, 255, 255, 0.9);
            padding: 2rem;
            border-radius: 10px;
        }
        .stApp {
            background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
        }
        .stButton > button {
            background-color: #ff6f61;
            color: white;
            font-weight: bold;
            border: None;
            border-radius: 6px;
            padding: 10px 20px;
        }
        .stTextInput > div > div > input,
        .stTextArea textarea {
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fffaf0;
        }
        .stMarkdown h1 {
            color: #ff6f61;
        }
        .stMarkdown h2 {
            color: #d72638;
        }
        .stMarkdown h3 {
            color: #3b3b98;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize the database
init_db()

# Page Configuration
st.title("📇 Personal CRM via LLM: AI-Driven Networking Assistant")

# File Upload Section
st.subheader("📤 Upload Business Card or PDF")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    file_path = save_uploaded_file(uploaded_file)

    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        extracted_text = extract_text_from_image(file_path)
    elif uploaded_file.type == "application/pdf":
        extracted_text = extract_text_from_pdf(file_path)

    st.subheader("📝 Extracted Text")
    st.text_area("Text from File", extracted_text, height=200)

    contact = extract_contact_entities(extracted_text)
    st.subheader("🔍 Extracted Contact Details")
    st.write(contact)

    if st.button("💾 Save Contact"):
        if contact['name'] and contact['email']:
            insert_contact(contact['name'], contact['email'], contact['phone'], contact['company'], "")
            st.success(f"✅ Contact '{contact['name']}' saved successfully!")
        else:
            st.error("⚠️ Failed to extract valid contact details!")

# View Saved Contacts
st.subheader("📚 Saved Contacts")
contacts = get_all_contacts()
if contacts:
    for contact in contacts:
        st.write(f"**Name:** {contact[1]}")
        st.write(f"**Email:** {contact[2]}")
        st.write(f"**Phone:** {contact[3]}")
        st.write(f"**Company:** {contact[4]}")
        st.write(f"**LinkedIn URL:** {contact[5]}")
        st.markdown("---")
else:
    st.info("No contacts saved yet.")

# LinkedIn Profile Search and Message Generation
st.subheader("🔗 LinkedIn Integration")
name = st.text_input("Enter Name to Search LinkedIn Profile")
company = st.text_input("Enter Company (optional)")

if name:
    linkedin_url = generate_linkedin_url(name, company)
    st.markdown(f"[🔍 Search LinkedIn Profile]({linkedin_url})", unsafe_allow_html=True)

    message = generate_connection_message(name, company)
    st.subheader("💬 Generated Message")
    st.text_area("Message", message, height=150)
