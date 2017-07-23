#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""A shot at captioning image files in Python!"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

base_img = os.path.join(os.getcwd(), 'img', 'beaker_base.png')

if os.path.exists(base_img) and os.path.isfile(base_img):
    with Image.open(base_img) as imgfile:
        original = "O nome do sistema é GNU"
        meme = "I nimi di sistimi i GNI"

        # Load the image into the ImageDraw object
        draw = ImageDraw.Draw(imgfile)

        # Get the image size and set font
        height, width = imgfile.size
        f = ImageFont.truetype("/home/lucas/.fonts/Ubuntu.ttf", 28)

        # Calculate coordinates:
        center_width = width // 2

        # Draw text according to rules (center-up and center-down)
        draw.text((center_width, 0), original, font=f)
        draw.text((center_width, height), meme, font=f)

        # Saving the new image:
        imgpath = os.path.join(os.getcwd(), 'img', 'new_img.png')
        imgfile.save(imgpath)
        print("This is a {} by {} pixels image.".format(width, height))

else:
    print("Uh-oh! File not found!")
    print("You're at %s. Maybe you should check that." % os.getcwd())
