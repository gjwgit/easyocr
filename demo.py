# -*- coding: utf-8 -*-
#
# Time-stamp: <Monday 2020-07-20 16:25:27 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the GPLv3
# Author: Graham.Williams@togaware.com
#
# ml demo easyocr
#
# This demo is based on:
#
# https://github.com/JaidedAI/EasyOCR

# Use the cached models.

import os
os.environ["MODULE_PATH"] = "cache"

from mlhub.pkg import mlask, mlcat, mlpreview

mlcat("Easy OCR", """\
This is a very simple demo of EasyOCR from Jaided.ai. 
This demo will read an image from Wikipedia and recognise the text
in Simplified Chinese and English. Text in both languages is detected.

A window will pop up shortly to display the image.

When requested you can press Enter to continue to the analysis without
closing the image (making sure the console has focus rather than the image).
""")

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import re
import easyocr
import urllib

reader = easyocr.Reader(['ch_sim','en'])

path = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Toronto_-_ON_-_Cecil_Street.jpg/1200px-Toronto_-_ON_-_Cecil_Street.jpg"

mlpreview(path)
mlask(end="\n")

mlcat("Apply Models", """\
A detection model and recognition models are now being loaded and applied to the image.
The results will be displayed on each line, consisting of the certainty of the result,
the bounding boxe of the text, and the text identified.
""")
with urllib.request.urlopen(path) as url:
    img = url.read()
    result = reader.readtext(img)

for r in result:
    bb = re.sub("[,\[\]]", "", " ".join(map(str, r[0])))
    print(f'{round(r[2],2)},{bb},{r[1]}')

mlask(True, True)

mlcat("Next: Analyse Your Own Images", """\
A command line tool is provided to analyses your own images,
either from local files or from URLs.

$ ml ocr easyocr myimg.png
""")

      
