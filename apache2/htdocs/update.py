#!D:\anaconda3\python.exe
import cgi
import os
import ast

import win32file

print("Content-Type: text/html")  # HTML is following
print()

files = os.listdir('form_data')

query_string = cgi.FieldStorage()
pageId = query_string['id'].value
with open('form_data/' + pageId) as file:
    content = file.read()


print(f'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8-sig">
  <title>원신 돌파재료 정보</title>
  <link rel="stylesheet" href="table-style.css?ne">
</head>
<body>
<div id="wrapper">
  <div id="head">
    <header>
      <h1><a href="index.py" title="캐릭별 돌파/특성 재료">캐릭별 돌파/특성 재료</a></h1>
    </header>
    <nav>
      <ul id="menu_list">
        <li class="list_item"><a href="index.py">캐릭터 돌파재료</a></li>
        <li class="list_item"><a href="form.py">문의</a></li>
      </ul>
    </nav>
  </div>
  <form action="form_update.py" method="post">
    <input type="hidden" name="pageId" value="{pageId}">
    <p><input type="text" name ="title" placeholder="제목" value="{pageId}"></p>
    <p><textarea name="content" placeholder="내용">{content}</textarea></p>
    <p><input type="submit"></p>
  </form>


</div>


</body>
</html>

''')
