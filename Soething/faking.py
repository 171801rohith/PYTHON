import fitz # PyMuPDF

# doc = fitz.open("R:/MOVIES/BOOKS/Never-Lie-By-Freida-McFadden.pdf")
# text = ""
# for page in doc:
#     text += page.get_text()
# print(text)


import random
import pandas as pd
from faker import Faker

fake = Faker()

def generate_record(employee_id):
    return {
        "EmployeeId": str(employee_id),
        "DateWorked": fake.date_between(start_date="-90d", end_date="today").isoformat(),
        "JobCode": f"JOB{random.randint(100,999)}",
        "CostCode": str(random.choice([f"{i:04d}" for i in range(400, 500)])),
        "PayType": random.choice(["REG", "OT", "DT"]),  # Regular, Overtime, Double-time
        "HoursWorked": random.choice([4, 6, 8, 10, 12]),
        "WorkOrder": f"WO{random.randint(100,999)}",
        "Department": random.choice(["FieldOps", "Maintenance", "Logistics", "Safety"]),
        "Notes": random.choice([
            "Day shift", "Night shift", "Weekend work",
            "Emergency call", "Regular schedule", "Overtime"
        ])
    }

# Generate 2000 records
records = [generate_record(random.randint(100, 999)) for _ in range(2000)]

# Convert to DataFrame
df = pd.DataFrame(records)

# Save to CSV
df.to_csv("fake_timesheets.csv", index=False)

print("✅ Generated 2000 fake records and saved to fake_timesheets.csv")
