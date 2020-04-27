# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:29:52 2020

@author: Nishidh Shekhawat
"""

#! /usr/bin/env python3
import os
import requests

filepath = "~/supplier-data/descriptions"
filepath = os.path.expanduser(filepath)
files=os.listdir(filepath)
dict_desc = {}

def read_file():
  for file_name in files:
    with open(filepath+'/' +file_name, "r") as file:
      dict_desc["name"] = file.readline().rstrip()
      dict_desc["weight"] = int(file.readline().split(" ")[0])
      dict_desc["description"] = file.readline().rstrip()
      dict_desc["image_name"] = file_name[:-4] + ".jpeg"
    #print(dict_desc)
    post_dict(dict_desc)

def post_dict(dict_data):
  response = requests.post("http://35.238.42.6/fruits/", json=dict_data)
  if response.status_code == 201:
    print("Post to site successful for : ",dict_data["name"])
  else:
    print("Error while posting : " + dict_data['name'] + ", error code : " + str(response.st$

if __name__ == "__main__":
  read_file()






