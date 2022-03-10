#!D:\anaconda3\python.exe
# -*-coding:utf-8-*-

import cgi
import os
import ast

form = cgi.FieldStorage()
title = form["title"].value
content = form["content"].value

opened_file = open('form_data/' + title, 'w')
opened_file.write(content)
opened_file.close()

print("Location: form.py")  # HTML is following
print()