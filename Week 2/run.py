# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 15:36:10 2020

@author: Nishidh Shekhawat
"""
#! /usr/bin/env python3
import os
import requests

filepath = '/data/feedback'
files=os.listdir(filepath)
dict_reviews = {}

def read_file():
  for file_name in files:
    with open(filepath+'/' +file_name, "r") as file:
      dict_reviews["title"] = file.readline().rstrip()
      dict_reviews["name"] = file.readline().rstrip()
      dict_reviews["date"] = file.readline().rstrip()
      dict_reviews["feedback"] = file.readline().rstrip()
    #print(dict_reviews)
    post_dict(dict_reviews)

def post_dict(dict_data):
  response = requests.post("http://34.67.0.150/feedback/", json=dict_data)
  if response.status_code == 201:
    print("Post to site successful for : ",dict_data["title"])
  else:
    print("Error while posting : " + dict_data['title'] + ", error code : " + str(response.status_code))

if __name__ == "__main__":
  read_file()

