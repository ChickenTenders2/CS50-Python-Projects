import sys
from PIL import Image, ImageOps

image_formats = (".jpg", ".jpeg", ".png") #tuple of strings

if len(sys.argv) == 3:
    before = sys.argv[1]
    after = sys.argv[2]
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:
    if before.lower().endswith(image_formats) and after.lower().endswith(image_formats):
        name1, format1 = before.split(".")
        name2, format2 = after.split(".")
    else:
        sys.exit("Input does not exist")
    if format1 != format2:
        sys.exit("Input and output have different extensions")
except FileNotFoundError:
    sys.exit("Invalid output")

try:
    with Image.open(before) as student:
        with Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            student = ImageOps.fit(student, shirt_size)
            student.paste(shirt, box=(0, 0), mask=shirt) #box is the top-left corner of the shirt, mask perserves the transparency of the shirt
            student.save(after, format=None)
except FileNotFoundError:
    sys.exit("Invalid output")
