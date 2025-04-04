import sys
import csv
from tabulate import tabulate

items = []

if len(sys.argv) == 2:
    doc = sys.argv[1]
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if doc.endswith(".csv"):
        with open(doc) as file:
            reader = csv.reader(file)
            for pizza, small, large in reader:
                items.append({"pizza": pizza, "small": small, "large": large})
            print(tabulate(items, headers="firstrow", tablefmt="grid"))
    else:
        sys.exit("Not a CSV file")
except FileNotFoundError:
    sys.exit("File does not exist")


