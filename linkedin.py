import urllib.parse

def generate_linkedin_url(name, company=None):
    query = name
    if company:
        query += f" {company}"
    query += " site:linkedin.com/in"
    search_url = f"https://www.google.com/search?q={urllib.parse.quote_plus(query)}"
    return search_url

def generate_connection_message(name=None, context=None):
    greeting = f"Hi {name}," if name else "Hi,"
    body = "I came across your profile and would love to connect."
    if context:
        body += f" I noticed your work at {context} and found it very impressive."
    closing = "Looking forward to connecting!"
    return f"{greeting}\n\n{body}\n\n{closing}"
