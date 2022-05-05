import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://e-book.hufs.ac.kr/20220214_freshman_h2/"

req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()

soup = BeautifulSoup(res, 'html.parser')
soup = soup.find("div", id_="EBooks")
# img의 경로를 받아온다
imgUrl = soup.find("img")["src"]

# urlretrieve는 다운로드 함수
# img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')
