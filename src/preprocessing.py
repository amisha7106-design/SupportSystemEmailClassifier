def preprocess_email(email: str) -> str:

    email = email.lower()
    email = email.strip()
    return email
import csv
from pathlib import Path

def process_csv():
    base_dir = Path(__file__).resolve().parent.parent
    input_file = base_dir / "data" / "raw" / "email.csv"
    output_file = base_dir / "data" / "processed" / "email.csv"

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(input_file, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    for row in rows:
        row["email"] = preprocess_email(row["email"])

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["email", "severity"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Processed CSV saved: {output_file}")


if __name__ == "__main__":
    process_csv()