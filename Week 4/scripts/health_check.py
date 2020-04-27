# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:28:05 2020

@author: Nishidh Shekhawat
"""

#!/usr/bin/env python3

import psutil
import shutil
import emails
import requests
import os

def cpu_check():
  usage = psutil.cpu_percent(1)
  cpu_usage = [usage * 100, (1-usage) * 100]
  print(cpu_usage)
  return usage < 80

def disk_check():
  diskutl = shutil.disk_usage('/')
  free = diskutl.free / diskutl.total * 100
  print(free)
  return free > 20

def memory_check():
  usage = psutil.virtual_memory()
  print(usage[1] >> 20)
  usage = usage[1] >> 20
  return usage > 500

def hostname_check():
  host = "http://127.0.0.1"
  req = requests.get(host)
  return req.status_code == 200

error_message=""
if __name__ == "__main__":

  if not cpu_check():
    error_message = "Error - CPU usage is over 80%"
  if not disk_check():
    error_message = "Error - Available disk space is less than 20%"
  if not memory_check():
    error_message = "Error - Available memory is less than 500MB"
  if not hostname_check():
    error_message = "Error - localhost cannot be resolved to 127.0.0.1"

  if error_message != "":
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = error_message
    body = "Please check your system and resolve the issue as soon as possible."

    email = emails.generate_email(sender, receiver, subject, body, "")
    emails.send_email(email)

