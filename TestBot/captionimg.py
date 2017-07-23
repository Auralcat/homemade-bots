#!/usr/bin/python3
# -*- encoding: utf-8 -*-

"""A shot at captioning image files in Python!"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

imgpath = os.path.join(os.getcwd(), 'img')
base_img = os.path.join(os.getcwd(), 'img', 'beaker_base.png')
if os.path.exists(imgpath) and os.path.isfile(imgpath):
    with Image.open(imgpath) as imgfile:
        caption = "This is a caption."
        draw = ImageDraw.Draw(imgfile)
        f = ImageFont.truetype("/home/lucas/.fonts/Ubuntu.ttf", 32)
        draw.text((4, 0), caption, font=f)
        imgfile.save(imgpath)

else:
    print("Uh-oh! Directory not found!")
    print("You're at %s. Maybe you should check that." % os.getcwd())
