html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>멀티 캠퍼스 마켓</title>
</head>
<body>
    <h1> 멀캠 마켓_mulcam_market</h1>
    <div calss="sale">
        <p id="fruits1" class = "fruits">
            <span class = "name"> 바나나 </span>
            <span class = "price">3000원</span>
            <span class = "inventory">500개</span>
            <span class = "store">선릉센터</span>
            <a href="http://google.co.kr">홈페이지</a>
        </p>
    </div>
    <div class = "prepare">
        <p id = "fruits" class = "fruits">
            <span class="name"> 파인애플 </span>
        </p>
    </div>
</body>
</html>

'''

#bs4 : beautifulsoup 정적(static) 웹문서를 파싱(parsing) 하는 툴 (tool)

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')
print(soup)

# print(soup.select('span'))
# print(soup.select('span')[0]) --> <span class="name">바나나</span>
# print(soup.select('span')[-1]) --> <span class="name">파인애플</span>

# '#' : id(아이디), '.' : 클래스 

# print(soup.select('#fruits1'))
'''[<p class="fruits" id="fruits1">
<span class="name">바나나</span>
<span class="price">3000원</span>
<span class="inventory">500개</span>
<span class="store">선릉센터</span>
<a href="http://google.co.kr">홈페이지</a>
</p>]'''

#print(soup.select('.price')) --> [<span class="price">3000원</span>]

# print(soup.select('span.name')) 
# --> [<span class="name">바나나</span>, <span class="name">파인애플</span>]

# tags = soup.select('span.name')
# print(tags[0])
# print(tags[1])
#--> <span class="name">바나나</span>
#    <span class="name">파인애플</span>

name_tags = soup.select('.name')
# print(name_tags[0])
# print(name_tags[1])
#--> <span class="name">바나나</span>
#    <span class="name">파인애플</span>

# print(name_tags[0].text) #바나나
# print(name_tags[1].text) #파인애플

# print(name_tags[0].text.strip()) #깔끔하게 
# print(name_tags[1].text.strip()) 

for tag in name_tags:
    print(tag.text.strip())

