#!D:\anaconda3\python.exe
print("Content-Type: text/html")    # HTML is following
print()

print('''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>원신 돌파재료 정보</title>
  <link rel="stylesheet" href="css/table-style.css">
</head>
<body>
<div id="wrapper">
  <div id="header">
    <h1><a href="home.html" title="캐릭별 돌파/특성 재료">캐릭별 돌파/특성 재료</a></h1>
  </div>
  <div id="grid">

    <ul class="table">
      <a href="zhongli.html" title="종려">
        <li id="zhongli">종려</li>
      </a>
      <a href="raiden-shogun.html" title="라이덴 쇼군">
        <li id="raiden-shogun">라이덴 쇼군</li>
      </a>
    </ul>
    <div id="article">
      <p>
        <- 클릭하면 나옴
      </p>
    </div>
  </div>


</div>


</body>
</html>
''')