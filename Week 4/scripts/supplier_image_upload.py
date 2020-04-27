# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:28:05 2020

@author: Nishidh Shekhawat
"""
#supplier_image_upload.py
#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = '~/supplier-data/images'
path = os.path.expanduser(path)
file_names = os.listdir(path)

for file in file_names:
  if file[-4:] == 'jpeg':
    with open(path + '/' + file, 'rb') as opened:
      print("Uploading file : " + file)
      r = requests.post(url, files={'file': opened})
  else:
    print("Skipping file : " + file)
