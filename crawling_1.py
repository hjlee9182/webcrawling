import urllib.request
import bs4

url  = "https://news.naver.com/"
html = urllib.request.urlopen(url)

bs_obj = bs4.BeautifulSoup(html,"html.parser")

newsnow_txarea = bs_obj.find("ul",{"class":"newsnow_txarea"})
lis = newsnow_txarea.findAll("li")

for li in lis:
    a = li.find("a")
    strong = a.find("strong")
    print(strong.text)
