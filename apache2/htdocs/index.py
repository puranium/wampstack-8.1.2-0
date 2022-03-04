#!D:\anaconda3\python.exe
import cgi
import os

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
    description = open('data/' + page_id, 'r', encoding='utf-8').read()
else:
    page_id = 'Welcome'
    description = ' <- 클릭해주세요'

print('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8-sig">
  <title>원신 돌파재료 정보</title>
  <link rel="stylesheet" href="table-style.css">

</head>
<body>
<div id="wrapper">
  <div id="header">
    <h1><a href="index.py" title="캐릭별 돌파/특성 재료">캐릭별 돌파/특성 재료</a></h1>
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
