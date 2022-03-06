#!D:\anaconda3\python.exe
import cgi
import os
import ast

print("Content-Type: text/html")  # HTML is following
print()

files = os.listdir('data')
CharList = ''
for item in files:
    CharList = CharList + '<a href="index.py?id={char_name}" title="{char_name}"><li id="char">{char_name}</li></a>'.format(
        char_name=item)

form = cgi.FieldStorage()
if 'id' in form:
    page_id = form["id"].value
    with open('data/' + page_id, 'r') as f:
        data = f.read()
    material = ast.literal_eval(data)
    description = material['Mat1'] + ' ' + material['Mat2'] + ' ' + material['Mat3'] + ' ' + material['Mat4']
else:
    page_id = 'Welcome'
    description = ' <- 클릭해주세요'

print('''<!DOCTYPE html>
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
  <div id="grid">

    <ul class="table">
      {CharList}
    </ul>
    <div id="article">
      <p>
        {desc}
      </p>
    </div>
  </div>


</div>


</body>
</html>

'''.format(char_name=page_id, CharList=CharList, desc=description))
