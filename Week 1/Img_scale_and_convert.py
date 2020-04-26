# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:35:52 2020

@author: Nishidh Shekhawat
"""

#!/usr/bin/env python3
from PIL import Image
import os

path = 'images'
new_path = '/opt/icons'
file_names = os.listdir(path)

for file in file_names:
  try:
    with Image.open(file) as im:
      im = Image.open(path + '/' + file)
      im.rotate(-90).resize((128,128)).convert("RGB").save(new_path + '/' + file, format="jpeg")
      im.close()
  except IOError:
    pass
