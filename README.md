**The_Developers_arena_task_3--Database-Management-APIs**

*End-to-end Weather Data Pipeline with Python, SQLite, ETL, and OpenWeatherMap API, including automated reporting.*


**🌦️ Weather Data Pipeline System**

📌 Project Overview

This project is an end-to-end Weather Data Pipeline System built using Python, SQLite, and the OpenWeatherMap API.

The system:

Extracts real-time weather data from OpenWeatherMap API

Transforms and validates the data

Loads it into a SQLite database

Generates automated reports with analytics

Supports both mock data and live API data

Demonstrates a complete ETL (Extract, Transform, Load) workflow

This project was built as part of Task 3 – Database Management & APIs.

🎯 Objectives

Build a complete data engineering pipeline

Integrate external API (OpenWeatherMap)

Design a normalized SQLite database (3+ tables)

Implement ETL with error handling

Generate analytical reports

Provide proper documentation and structure for submission

🏗️ System Architecture
OpenWeatherMap API
        ↓
   api_client.py
        ↓
   etl_pipeline.py
        ↓
   SQLite Database (weather_data.db)
        ↓
     reporter.py
        ↓
   Text Report in /reports folder

📁 Project Structure
task3/
├── src/
│   ├── api_client.py        # Fetches weather data from API
│   ├── etl_pipeline.py      # Runs ETL pipeline (Extract, Transform, Load)
│   ├── database.py          # Creates database and tables
│   ├── reporter.py          # Generates analytics report
│
├── database/
│   └── weather_data.db      # SQLite database file
│
├── reports/
│   └── weather_report_*.txt # Generated reports
│
├── docs/
│   ├── etl_run.png          # Screenshot of ETL running
│   ├── report_output.png    # Screenshot of report output
│   ├── database_file.png    # Screenshot of database file
│   └── report_file.png      # Screenshot of report file
│
├── config/
│   └── config.json          # API key configuration file
│
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
└── .gitignore

🧰 Technologies Used

Python 3

SQLite

Requests (HTTP library)

OpenWeatherMap API

🔑 API Integration

This project uses the OpenWeatherMap API to fetch real-time weather data.

Endpoint Used:
https://api.openweathermap.org/data/2.5/weather

Example API Call:
https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=YOUR_API_KEY&units=metric

Configuration

Create a file:

config/config.json


Add:

{
  "OPENWEATHER_API_KEY": "YOUR_API_KEY_HERE"
}

🗄️ Database Design (SQLite)

The database file is located at:

database/weather_data.db

Tables (Normalized)

cities

id (PK)

name

country

weather_data

id (PK)

city_id (FK)

timestamp

temperature_c

humidity

pressure_hpa

wind_speed_mps

weather_condition

(Optional / Can be extended) etl_logs

id

run_time

status

message

This satisfies the requirement of 3+ normalized tables.

🔄 ETL Workflow
Extract

Fetches weather data for multiple cities using api_client.py

Transform

Validates data

Extracts:

Temperature

Humidity

Pressure

Wind speed

Weather condition

Adds timestamp

Load

Inserts cleaned data into SQLite database (weather_data table)

⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup Database
python src/database.py


This will:

Create the database

Create tables

Insert initial cities

▶️ How to Run the Project
Run ETL Pipeline (Live API Data)
python src/etl_pipeline.py


Expected output:

🚀 Running ETL Pipeline (Live API Data)...
✅ Inserted live weather for Mumbai
✅ Inserted live weather for Delhi
...
🎉 ETL Pipeline completed with live data!

Generate Report
python src/reporter.py


Output:

A report file will be created in:

reports/weather_report_YYYYMMDD_HHMMSS.txt

📊 Report Contents

The report includes:

Total records in database

Average temperature per city

Latest weather snapshot for each city

📸 Screenshots

Screenshots are stored in the docs/ folder:

ETL pipeline running

Report generation output

Database file

Generated report file

These are included for submission proof.

🧪 Error Handling & Logging

API errors are handled (e.g., 401, network issues)

Missing or invalid data is skipped safely

Console messages show success/failure for each city

ETL continues even if one city fails

🛠 Troubleshooting
❌ 401 Unauthorized Error

Your API key is not active yet OR invalid

Wait a few hours after generating key

Check config.json and API key value

❌ no such table: weather_data

Run:

python src/database.py


First to create tables.

❌ Module not found

Run:

pip install -r requirements.txt

✅ How This Project Meets Requirements

✔ Uses OpenWeatherMap API
✔ Implements complete ETL pipeline
✔ Uses SQLite with normalized tables
✔ Has API client module
✔ Has automated reporting
✔ Has error handling
✔ Has proper folder structure
✔ Has documentation & screenshots
✔ Ready for GitHub submission

🚀 Future Improvements

Add scheduling (cron / task scheduler)

Add dashboard (Streamlit / Power BI)

Add more cities

Add ETL logging table

Export reports to CSV / PDF

👤 Author

Your Name
Task 3 – Database Management & APIs


