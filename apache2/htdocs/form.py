#!D:\anaconda3\python.exe
import cgi
import os
import html_sanitizer
sanitizer = html_sanitizer.Sanitizer

print("Content-Type: text/html")  # HTML is following
print()

files = os.listdir('form_data')
formList = ''
for item in files:
    formList = formList + f'<a href="form.py?id={item}" title="{item}"><li>{item}</li></a>'

query_string = cgi.FieldStorage()
if 'id' in query_string:
    pageId = query_string['id'].value
    update_action = f'''
        <form action = "update.py?id={pageId}" method ="post">
            <input type="submit" value="수정">
        </form>
    
    '''
    delete_action = f'''
        <form action = "form_delete.py" method ="post">
            <input type="hidden" name="pageId" value="{pageId}">
            <input type="submit" value="삭제">
        </form>
    
    '''
    with open('form_data/' + pageId) as file:
        file_data = file.read()
        content = f'''<div> 
            <h3>{pageId}</h3>
            <p>{file_data}</p>
            <p style="color:black;">{update_action}{delete_action}</p>
        </div>'''
else:
    content = f'''<form action="form_answer.py" method="post">
        <p><input type="text" name ="title" placeholder="제목"></p>   
        <p><textarea name="content" placeholder="내용"></textarea></p>
        <p><input type="submit"></p>
    </form>
    <ul>{formList}</ul>'''

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
  {content}


</div>


</body>
</html>

''')
