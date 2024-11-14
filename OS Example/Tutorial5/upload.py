import csv

logs = [
    {
        "account_number": 123,
        "amount": 1234,
        "transaction_type": "deposit",
        "datetime": "20 - 13 - 65",
        "to_account_number": 986,
    },
    {
        "account_number": 13,
        "amount": 1664,
        "transaction_type": "weposit",
        "datetime": "2 - 13 - 65",
        "to_account_number": 976,
    },
    {
        "account_number": 12376,
        "amount": 12334,
        "transaction_type": "transfer",
        "datetime": "20 - 3 - 65",
        "to_account_number": 876,
    },
]

with open("Log.csv", "w", newline="") as f:
    fields = [
        "account_number",
        "amount",
        "transaction_type",
        "datetime",
        "to_account_number",
    ]
    csv_writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t")
    csv_writer.writeheader()  # Write header row

    for line in logs:
        # row = dict(zip(fields, line))  # Convert list to dictionary
        csv_writer.writerow(line)
