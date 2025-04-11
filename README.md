# 🔗 URL Shortener API

A simple URL shortener API built using FastAPI and SQLAlchemy with async support. It allows you to shorten long URLs and redirect using the short code.



##  Project Structure


url_shortener/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   └── utils.py
|           
├── requirements.txt
└── README.md


##  Features

- Shorten long URLs with a generated short code
- Redirect to the original URL using the short code
- Clean and modular project structure
- CORS support for frontend integration


##  Installation

```bash
# Clone the repo
$ git clone https://github.com/yourname/url_shortener
$ cd url_shortener

# Create virtual environment & install dependencies
$ python -m venv venv
$ source venv/bin/activate  
$ pip install -r requirements.txt
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root:

```
DATABASE_URL=your_database_connection_string
```



## Usage

Start the server:

```bash
uvicorn app.main:app --reload
```

### API Endpoints

- `POST /shorten` — Shortens a given long URL
- `GET /{short_code}` — Redirects to the original URL

---

##  Sample Request (POST /shorten)

**Request Body:**
```json
{
  "long_url": "https://www.example.com"
}
```

**Response:**
```json
{
  "short_url": "http://localhost:8000/abc123"
}
```

Copy the `short_url` from the response and paste it directly into your browser to test redirection.
Do **not** use `/short_code` path manually — just search or open the given short URL in a browser.

---
