from pyfiglet import Figlet
import sys, random

if len(sys.argv) < 2 or sys.argv[1] not in ['-f', '--font']:
    sys.exit()

figlet = Figlet()

try:
    fonts = figlet.getFonts()
    if len(sys.argv) == 3:
        font = figlet.setFont(font=sys.argv[2])
        response = input("Input: ")
        print(f"Output: {figlet.renderText(response)}")
    elif len(sys.argv) == 1:
        random_font = random.choice(fonts)
        font = figlet.setFont(font=random_font)
        response = input("Input: ")
        print(f"Output: {figlet.renderText(response)}")
except ValueError:
    sys.exit()
