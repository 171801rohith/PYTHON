import csv
import json

# Function to convert CSV to JSONL
def csv_to_jsonl(csv_file, jsonl_file):
    with open(csv_file, mode="r", encoding="utf-8") as f_in, open(jsonl_file, mode="w", encoding="utf-8") as f_out:
        reader = csv.DictReader(f_in)
        for row in reader:
            f_out.write(json.dumps(row) + "\n")  # one object per line

# Example usage
csv_to_jsonl("final_training_data.csv", "output.jsonl")
