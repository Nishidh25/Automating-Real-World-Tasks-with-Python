# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:29:52 2020

@author: Nishidh Shekhawat
"""

#!/usr/bin/env python3
import os
import datetime
import reports
import emails

today = datetime.date.today()
today = today.strftime("%A") + " " + today.strftime("%d") + ", " + today.strftime("%Y")

filepath = os.path.expanduser("~/supplier-data/descriptions/")

def gen_pdf():
  title = "Processed Update on " + today
  paragraph = ""
  for file in os.listdir(filepath):
    with open(filepath + file) as item:
      paragraph += "name: " + item.readline().rstrip() + "<br/>"
      paragraph += "weight: " + item.readline().rstrip() + "<br/><br/>"
  new_file = "/tmp/processed.pdf"
  return new_file, title, paragraph


if __name__ == "__main__":
  new_file, title, paragraph = gen_pdf()
  reports.generate_report(new_file, title, paragraph)


  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  attachment = new_file
  new_email = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(new_email)

