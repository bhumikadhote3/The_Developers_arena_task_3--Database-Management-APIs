import sqlite3
from datetime import datetime
from api_client import fetch_weather

DB_PATH = "database/weather_data.db"

CITIES = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]


def get_city_id(cursor, city_name):
    cursor.execute("SELECT city_id FROM cities WHERE city_name = ?", (city_name,))
    result = cursor.fetchone()
    return result[0] if result else None


def run_etl():
    print("🚀 Running ETL Pipeline (Live API Data)...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    for city in CITIES:
        data = fetch_weather(city)

        if not data or "main" not in data:
            print(f"❌ Skipping {city}, no data")
            continue

        city_id = get_city_id(cursor, city)
        if not city_id:
            print(f"❌ City not found in DB: {city}")
            continue

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["description"]
        timestamp = datetime.now()

        cursor.execute("""
            INSERT INTO weather_data (
                city_id, timestamp, temperature_c, humidity, pressure_hpa, wind_speed_mps, weather_condition
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (city_id, timestamp, temperature, humidity, pressure, wind_speed, condition))

        print(f"✅ Inserted live weather for {city}")

    conn.commit()
    conn.close()
    print("🎉 ETL Pipeline completed with live data!")


if __name__ == "__main__":
    run_etl()
