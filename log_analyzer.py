import logging
from collections import Counter
from datetime import datetime

LOG_FILE = "app.log"


def setup_logger():
    logging.basicConfig(
        filename=LOG_FILE,
        filemode="a",  # append
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def generate_sample_logs():
    # This is just to create data for your analyzer (you can delete later).
    logging.info("Program started")
    logging.info("User opened menu")
    logging.warning("Low disk space warning (sample)")
    logging.error("Failed to load settings file (sample)")
    logging.info("User clicked analyze logs")
    logging.info("Program finished")


def parse_log_line(line):
    # Expected format: "YYYY-MM-DD HH:MM:SS | LEVEL | message"
    parts = line.strip().split(" | ", 2)
    if len(parts) != 3:
        return None

    ts_str, level, message = parts
    try:
        ts = datetime.strptime(ts_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return None

    return ts, level, message


def analyze_log_file():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Log file '{LOG_FILE}' not found. Run the program once to create it.")
        return

    records = []
    for line in lines:
        parsed = parse_log_line(line)
        if parsed:
            records.append(parsed)

    if not records:
        print("No valid log records found.")
        return

    level_counts = Counter(level for _, level, _ in records)
    message_counts = Counter(message for _, _, message in records)

    times = [ts for ts, _, _ in records]
    start_time = min(times)
    end_time = max(times)

    print("\n--- Log Analyzer Report ---")
    print(f"Log file: {LOG_FILE}")
    print(f"Total records: {len(records)}")
    print(f"Time range: {start_time}  to  {end_time}")

    print("\nCounts by level:")
    for lvl in ["INFO", "WARNING", "ERROR", "CRITICAL", "DEBUG"]:
        if lvl in level_counts:
            print(f"  {lvl}: {level_counts[lvl]}")

    print("\nTop 5 messages:")
    for msg, count in message_counts.most_common(5):
        print(f"  ({count}) {msg}")


def main():
    setup_logger()

    print("Logging + Log Analyzer")
    print("1. Generate sample logs")
    print("2. Analyze log file")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        generate_sample_logs()
        print(f"Sample logs written to {LOG_FILE}")
    elif choice == "2":
        analyze_log_file()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()