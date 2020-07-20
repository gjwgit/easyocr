# -*- coding: utf-8 -*-
#
# Time-stamp: <Monday 2020-07-20 15:39:07 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the GPLv3
#
# A command line to extract text from an image.
#
# ml ocr easyocr <path> [-l <lang> ...]

# Use the cached models.

import os
os.environ["MODULE_PATH"] = "cache"

# Import the required libraries.

import re
import sys
import easyocr
import argparse
import requests
import urllib

from mlhub.pkg import is_url
from mlhub.utils import get_cmd_cwd

# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    "-l",
    "--lang",
    nargs='+',
    type=str,
    help="languages to identify",
)

option_parser.add_argument(
    'path',
    help='path or url to image'
)

args = option_parser.parse_args()

path = args.path
lang = args.lang if args.lang else ['en']

# Avoid the stderr message:
# CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.

#stderr  = sys.stderr
#sys.stderr = open(os.devnull, 'w')
reader= easyocr.Reader(lang_list=lang)
#sys.stderr = stderr

if is_url(path):
    request = requests.get(path)
    if request.status_code != 200:
        print(f"The URL does not appear to exist. Please check.")
        print(f"    {path}")
        quit()
    with urllib.request.urlopen(path) as url:
        img = url.read()
        result = reader.readtext(img)

#        bytearray,
#        lambda x: np.asarray(x, dtype="uint8"),
#        lambda x: cv.imdecode(x, cv.IMREAD_GRAYSCALE))
#    rawHttpResponse = client.read(path, raw=raw)
else:
    path = os.path.join(get_cmd_cwd(), path)
    result = reader.readtext(path)

# Print result.

for r in result:
    bb = re.sub("[,\[\]]", "", " ".join(map(str, r[0])))
    print(f'{round(r[2],2)},{bb},{r[1]}')

