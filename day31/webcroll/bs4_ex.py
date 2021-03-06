# BeautifulSoup 사용하기 - html 태그 및 데이터 추출 라이브러리

from bs4 import BeautifulSoup

html_str = """
<html>
    <body>
        <ul class="item">
            <li>인공 지능</li>
            <li>빅데이터</li>
            <li>로봇공학</li>
        </ul>
        <ul class="lang">
            <li>Python</li>
            <li>C/C++</li>
            <li>Java</li>
        </ul>
    </body>
</html>
"""

html = BeautifulSoup(html_str, "html.parser")
first_ul = html.find('ul')
print(first_ul)
print(first_ul.text)

