# PersonalCRM
# 🧠 Personal CRM via LLM  
**AI-Driven Private Networking Assistant**

A privacy-focused, AI-powered contact management tool that extracts information from business cards and PDFs, stores them locally, and helps you connect on LinkedIn with personalized messages — all through a beautiful Streamlit interface.

---

## 📌 Features

- 📤 Upload business cards or PDFs (images or documents)
- 🔍 Extract name, email, phone, and company using OCR + NLP
- 🧠 AI-assisted contact entity recognition
- 💾 Save contacts locally using SQLite
- 🔗 Generate LinkedIn search URLs
- ✉️ Auto-generate personalized LinkedIn messages
- 🎨 Sleek, vibrant, and professional UI

---

## 🧰 Tech Stack

| Category      | Tools / Libraries                          |
|---------------|---------------------------------------------|
| **Frontend**  | Streamlit                                   |
| **Backend**   | Python, SQLite                              |
| **AI/NLP**    | spaCy, Regex                                |
| **OCR**       | EasyOCR, PyMuPDF                            |
| **Utils**     | Custom File Handlers, LinkedIn Search Logic |

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/personal-crm-llm.git
cd personal-crm-llm
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On macOS/Linux
pip install -r requirements.txt
streamlit run app.py
```

> 📝 **Note**: Requires Python 3.9+ for compatibility with spaCy and other packages.

---

## 📂 Project Structure

```
personal-crm/
│
├── app.py               # Main Streamlit app
├── db.py                # SQLite DB functions
├── extractor.py         # OCR + Entity extraction
├── linkedin.py          # LinkedIn search + message generation
├── utils.py             # File saving & helper functions
├── requirements.txt     # Dependencies
└── README.md            # This file
```

---

## 🔒 Privacy & Security

- All data is stored **locally**.
- No third-party cloud APIs used.
- Built for **privacy-conscious professionals**.

---

## 📌 Roadmap

- [ ] Advanced contact search & filters  
- [ ] Google Contacts integration  
- [ ] Docker support  
- [ ] Web deployment (optional & secure)

---

## 🤝 Contribution

PRs and feedback are welcome! Open an issue or fork the repo to contribute.

---

## 📃 License

MIT License © 2025  
