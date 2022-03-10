#!D:\anaconda3\python.exe
# -*-coding:utf-8-*-

import cgi
import os
import ast

form = cgi.FieldStorage()
pageId = form["pageId"].value

os.remove('form_data/'+pageId)

print("Location: form.py")  # HTML is following
print()
