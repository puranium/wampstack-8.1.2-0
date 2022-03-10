#!D:\anaconda3\python.exe
# -*-coding:utf-8-*-

import cgi
import os
import ast

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
content = form["content"].value

os.rename('form_data/'+pageId, 'form_data/'+title)
opened_file = open('form_data/' + title, 'w')
opened_file.write(content)
opened_file.close()

print("Location: form.py")  # form.py를 열자
print()
