# The_Developers_arena_task_3--Database-Management-APIs
End-to-end Python ETL pipeline for weather data ingestion, transformation, storage in SQLite, and automated report generation, with support for OpenWeatherMap API integration.
🌦️ Weather Data ETL Pipeline
📌 Project Overview

This project is a Python-based ETL (Extract, Transform, Load) pipeline that collects weather data, stores it in a SQLite database, and generates analytical reports.

Due to API key activation delay, the pipeline currently uses mock weather data, but it is fully ready to switch to real OpenWeatherMap API data.

🛠️ Tech Stack

Python 3

SQLite

Requests (for API calls)

Virtual Environment (venv)

📂 Project Structure
task3/
│
├── src/
│   ├── database.py        # Creates database and tables
│   ├── api_client.py      # Fetches weather data from API
│   ├── etl_pipeline.py    # Runs ETL process (Extract, Transform, Load)
│   └── reporter.py        # Generates weather report
│
├── database/
│   └── weather_data.db    # SQLite database file
│
├── reports/
│   └── weather_report_YYYYMMDD_HHMMSS.txt
│
├── venv/                  # Virtual environment
└── README.md              # Project documentation

⚙️ Setup Instructions
1️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

2️⃣ Install Dependencies
pip install requests

🗄️ Step 1: Create Database
python src\database.py


✔ This will:

Create the SQLite database

Create required tables

Insert sample city records

🔁 Step 2: Run ETL Pipeline
python src\etl_pipeline.py


✔ This will:

Extract weather data (currently mock data)

Transform and validate data

Load data into the database

Insert records for multiple cities

📄 Step 3: Generate Report
python src\reporter.py


✔ This will:

Read data from the database

Generate a summary report

Save it in the reports/ folder

Show:

Total records

Average temperature per city

Latest weather snapshot

🌐 API Integration (Optional)

The project supports real OpenWeatherMap API integration.

In src/api_client.py, set:

API_KEY = "YOUR_REAL_API_KEY_HERE"


Once your API key is active, the pipeline can fetch real-time weather data instead of mock data.

📊 Sample Report Output

Total records in database

Average temperature per city

Latest weather snapshot per city

Timestamped report file in reports/ folder

✅ Features

End-to-end ETL pipeline

SQLite database storage

Automated report generation

Error handling and validation

Ready for real API integration

🚀 Future Improvements

Add charts/visualizations

Automate full pipeline run in one command

Add scheduling (daily data fetch)

Use real API data continuously

👨‍💻 Author

Built as part of a Python data engineering / ETL pipeline task.
