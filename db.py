import sqlite3

def init_db():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    phone TEXT,
                    company TEXT,
                    linkedin TEXT
                )''')
    conn.commit()
    conn.close()

def insert_contact(name, email, phone, company, linkedin):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, email, phone, company, linkedin) VALUES (?, ?, ?, ?, ?)",
              (name, email, phone, company, linkedin))
    conn.commit()
    conn.close()

def get_all_contacts():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    results = c.fetchall()
    conn.close()
    return results
