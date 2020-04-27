# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:27:10 2020

@author: Nishidh Shekhawat
"""
#!/usr/bin/env python3
from PIL import Image
import os

path = '~/supplier-data/images'
path = os.path.expanduser(path)
file_names = os.listdir(path)

for file in file_names:
  if file[-4:] != "tiff":
    print("Skipping non-tiff file " + file)
  else:
    img = Image.open(path + '/' + file)
    img.resize((600,400)).save(path + '/' + file[:-5] + '.jpeg')
