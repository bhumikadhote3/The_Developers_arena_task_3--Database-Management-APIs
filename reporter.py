import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join("database", "weather_data.db")
REPORTS_DIR = "reports"

def generate_report():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    report_lines = []
    report_lines.append("WEATHER DATA PIPELINE REPORT")
    report_lines.append("=" * 40)
    report_lines.append(f"Generated at: {datetime.now()}")
    report_lines.append("")

    # 1. Total records
    cursor.execute("SELECT COUNT(*) FROM weather_data")
    total_records = cursor.fetchone()[0]
    report_lines.append(f"Total records in database: {total_records}")
    report_lines.append("")

    # 2. Average temperature per city
    report_lines.append("Average Temperature per City:")
    cursor.execute("""
        SELECT c.city_name, ROUND(AVG(w.temperature_c), 2)
        FROM weather_data w
        JOIN cities c ON w.city_id = c.city_id
        GROUP BY c.city_name
    """)
    rows = cursor.fetchall()
    for city, avg_temp in rows:
        report_lines.append(f" - {city}: {avg_temp} °C")

    report_lines.append("")

    # 3. Latest weather snapshot
    report_lines.append("Latest Weather Snapshot:")
    cursor.execute("""
        SELECT c.city_name, w.temperature_c, w.humidity, w.timestamp
        FROM weather_data w
        JOIN cities c ON w.city_id = c.city_id
        ORDER BY w.timestamp DESC
        LIMIT 5
    """)
    rows = cursor.fetchall()
    for city, temp, humidity, ts in rows:
        report_lines.append(f" - {city}: {temp} °C, {humidity}% humidity at {ts}")

    conn.close()

    # Save report
    filename = f"weather_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    filepath = os.path.join(REPORTS_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

    print("📄 Report generated successfully!")
    print(f"📁 Saved to: {filepath}")
    print("\n".join(report_lines))


if __name__ == "__main__":
    generate_report()
