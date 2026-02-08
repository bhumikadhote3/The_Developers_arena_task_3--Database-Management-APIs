import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "database" / "weather_data.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    return conn


def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        city_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_name TEXT NOT NULL,
        country TEXT,
        latitude REAL,
        longitude REAL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather_data (
        record_id INTEGER PRIMARY KEY AUTOINCREMENT,
        city_id INTEGER,
        timestamp TIMESTAMP,
        temperature_c REAL,
        humidity INTEGER,
        pressure_hpa REAL,
        wind_speed_mps REAL,
        weather_condition TEXT,
        FOREIGN KEY (city_id) REFERENCES cities (city_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pipeline_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_time TIMESTAMP,
        status TEXT,
        message TEXT,
        records_processed INTEGER
    )
    """)

    conn.commit()
    conn.close()
    print("✅ Database and tables created successfully!")


def insert_city(city_name, country, lat, lon):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cities (city_name, country, latitude, longitude)
        VALUES (?, ?, ?, ?)
    """, (city_name, country, lat, lon))

    conn.commit()
    conn.close()
    print(f"✅ Inserted city: {city_name}")


def get_all_cities():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT city_id, city_name, country FROM cities")
    rows = cursor.fetchall()

    conn.close()
    return rows


if __name__ == "__main__":
    # Setup DB (safe to run multiple times)
    setup_database()

    # Insert some cities
    insert_city("Mumbai", "IN", 19.0760, 72.8777)
    insert_city("Delhi", "IN", 28.7041, 77.1025)
    insert_city("Bangalore", "IN", 12.9716, 77.5946)
    insert_city("Chennai", "IN", 13.0827, 80.2707)
    insert_city("Kolkata", "IN", 22.5726, 88.3639)

    # Fetch and print cities
    cities = get_all_cities()
    print("\n📍 Cities in Database:")
    for c in cities:
        print(c)
