Django Chatbot with SQL Agent

📌 Overview

This project is a chatbot interface built with Django that interacts with a PostgreSQL database using LangChain's SQL Agent. Users can input queries, and the chatbot will respond with relevant data retrieved from the database.

🚀 Features

Interactive chatbot UI with a modern design.

Uses LangChain SQL Agent to process and execute SQL queries.

Stores and fetches product data from PostgreSQL.

Implements CSRF protection for secure API requests.

📂 Project Structure

inventory_project/
│── inventory_project/      # Main Django project directory
│── inventory/              # Django app for chatbot
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   ├── chatbot_page.html
│   ├── views.py            # Django views (handles chatbot logic)
│   ├── urls.py             # URL routing
│   ├── sql_agent.py        # LangChain SQL Agent implementation
│── manage.py               # Django project manager

🔧 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/CodeWithRahul1/SqlAgentDjangoInventory.git
cd sql-agent-chatbot

2️⃣ Set Up Virtual Environment

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Configure Database

Update sql_agent.py with your PostgreSQL credentials:

DATABASE_URL = "postgresql+psycopg2://username:password@localhost/SqlAgentInventory"

Apply migrations:

python manage.py migrate

5️⃣ Run the Django Server

python manage.py runserver

Access the chatbot at: http://127.0.0.1:8000/inventory/chatbot/

🎨 Chatbot UI

Users and bot messages appear in rounded chat bubbles.

The input box width matches the chat window.

Uses AJAX to fetch responses dynamically.

🔥 API Endpoint

/inventory/query/
