# FastAPI Data Pipeline 🚀

## Overview
This project demonstrates a full-scale **data ingestion and processing pipeline** using **FastAPI** and **PostgreSQL**.  
It is designed to **read, process, and serve data** efficiently while maintaining a clean, modular architecture.

Key features:
- Modular project structure for scalability
- FastAPI backend for API endpoints
- Database integration with PostgreSQL
- Data ingestion services
- Static + template support for lightweight front-end rendering
- Version control using Git with SSH for secure collaboration

---

## 🗂 Project Structure

````text
fastapi-basics/
├── app/                 # FastAPI application entry point
│   └── main.py
├── db/                  # Database connection and schema
│   ├── connection.py
│   ├── push.py
│   └── schema.py
├── services/            # Business logic & data ingestion
│   └── ingest.py
├── static/              # CSS, JS, and static assets
│   └── style.css
├── templates/           # HTML templates for API responses
│   ├── index.html
│   └── result.html
├── requirements.txt     # Python dependencies
└── .gitignore           # Git ignore rules
`````

---

## ⚡ Features

* **Data Ingestion:** Handles multiple Excel/CSV sources seamlessly
* **Database Integration:** Stores processed data efficiently in PostgreSQL
* **API Endpoints:** Easily expose processed data using FastAPI
* **Modularity:** Clear separation between app logic, DB, and services
* **Version Control:** Secure Git workflow using SSH

---

## 💻 Installation & Setup

1. **Clone the repository**

```bash
git clone git@github.com:Jaskirat-2004/fastapi-basics.git
cd fastapi-basics
```

2. **Create a virtual environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure database**

* Update `db/connection.py` with your PostgreSQL credentials

5. **Run the FastAPI app**

```bash
uvicorn app.main:app --reload
```

---

## 📈 Future Scope

* Add **automated data validation** (e.g., using Great Expectations)
* Integrate **Airflow** for orchestration
* Add **user authentication** and API security
* Deploy to **cloud platforms** (AWS/GCP/Heroku)
* Build **interactive dashboards** for real-time insights

---

## 🔑 Key Learnings

* Setting up **FastAPI** project structure from scratch
* Writing modular Python code for data pipelines
* Using **Git & GitHub SSH** workflow for secure version control
* Integrating **PostgreSQL** database with Python
* Preparing projects ready for deployment and professional portfolio

---

## 📌 Author

**Jaskirat Singh** – Final Year Student & Aspiring Data Engineer/ML Developer
[LinkedIn](https://www.linkedin.com/in/jaskirat-link) | [GitHub](https://github.com/Jaskirat-2004)

