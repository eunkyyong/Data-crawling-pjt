import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/tag/life/'

# 1. 다운로드 - url을 이용해서 HTML이 담긴 자료를 받아와야 함
response = requests.get(url)

# html 문서를 text 형태로 확인
html_text = response.text

# str이 출력된다.
print(type(html_text))

# 문자열 파싱은 코드로 짜기 매우 복잡하다!
# 라이브러리를 쓰자!
soup = BeautifulSoup(html_text, 'html.parser')

# bs4.BeautifulSoup이 출력됨
print(type(soup))

# 1.  find
# - 첫 번째 태그를 가진 요소를 검색
main = soup.find('a')
print(main)

main1 = soup.find('title')
print(main1)

# 2. find_all
# - 해당 태그를 가진 모든 요소를 검색
# - list로 반환된다.
a_tags = soup.find_all('a')
print(a_tags)
# ,로 구분이 된 list에 담겨있다! -> F12 문서 구조만 잘 파악하면 된다!

# 3. select()
# - CSS 선택자를 사용하여 요소 검색. 모든 일치하는 요소를 리스트로 반환.

