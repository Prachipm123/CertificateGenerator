from PIL import Image, ImageFont, ImageDraw
import pandas as pd

# Global Variables
FONT_FILE = ImageFont.truetype(r'font/GreatVibes-Regular.ttf', 180)
# FONT_COLOR = "#FFFFFF"
FONT_COLOR = "#000000"

template = Image.open(r'template2.png')
WIDTH, HEIGHT = template.size

def make_certificates(name):
    '''Function to save certificates as a .png file'''

    image_source = Image.open(r'template2.png')
    draw = ImageDraw.Draw(image_source)

    # Finding the width and height of the text. 
    # name_width, name_height = draw.textsize(name, font=FONT_FILE)
    name_width = draw.textlength(name, font=FONT_FILE) 
    name_height = 180

    # Placing it in the center, then making some adjustments.
    draw.text(((WIDTH - name_width) / 2, (HEIGHT - name_height) / 2 - 30), name, fill=FONT_COLOR, font=FONT_FILE)

    # Saving the certificates in a different directory.
    image_source.save("./out/" + name +".png")
    print('Saving Certificate of:', name)        

if __name__ == "__main__":

    df = pd.read_csv("names.csv")
    
    names = [name for name in df]

    for name in names:
        make_certificates(name)

    print(len(names), "certificates done.")

