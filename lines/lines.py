import sys

lines = 0

if len(sys.argv) == 2:
    doc = sys.argv[1]
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    if doc.endswith(".py"):
        with open(doc, "r") as file:
            for line in file:
                if line.strip() == "":
                    continue
                elif line.strip().startswith("#"):
                    continue
                else:
                    lines += 1
            print(lines)
    else:
        sys.exit("Not a Python file")
except FileNotFoundError:
    sys.exit("File does not exist")


