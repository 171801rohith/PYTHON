import csv

# with open("nothing.csv", "r") as f:
#     csv_reader = csv.reader(f)
#     with open("noth.csv", "w")  as f:
#         csv_writer = csv.writer(f, delimiter="\t")

#         for line in csv_reader:
#             # print(line[3])
#             csv_writer.writerow(line)

with open("nothing.csv", "r") as f:
    csv_reader = csv.DictReader(f)
    with open("noth.csv", "w")  as f:
        fiednames = ['account_number', 'amount', 'transaction_type', 'datetime', 'to_account_number']
        csv_writer = csv.DictWriter(f, fieldnames=fiednames, delimiter="\t")
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)
    
