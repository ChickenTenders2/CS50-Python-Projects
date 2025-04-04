import sys
import csv

list = []

if len(sys.argv) == 3:
    doc = sys.argv[1]
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    if doc.endswith(".csv"):
        with open(doc) as file:
            reader = csv.reader(file)
            for name, house in reader:
                name = name.strip('""')
                if ", " in name:
                    last_name, first_name = name.split(",")
                    first_name = first_name.strip()
                    list.append({"first_name":first_name, "last_name":last_name, "house":house})
    else:
        sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

new_file = sys.argv[2]
with open(new_file, "w") as file:
    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for person in list:
        writer.writerow({"first": person["first_name"], "last": person["last_name"], "house": person["house"]})
