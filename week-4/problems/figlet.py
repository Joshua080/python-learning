import pyfiglet
import sys
import random

all_fonts = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    random_font = random.choice(all_fonts)
    print(pyfiglet.Figlet(font=random_font).renderText(text))

if len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in all_fonts:
        text = input("Input: ")
        print(pyfiglet.Figlet(font=sys.argv[2]).renderText(text))
    else:
        sys.exit("If you'd like to chose a font, please order your commands as follows: python figlet.py <'-f' or '--font'> <font name>")