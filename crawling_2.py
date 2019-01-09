import requests
from bs4 import BeautifulSoup

def get_bp_info(url) :

    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div",{"class":"profile-name"})

    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_button = bs_obj.find("div",{"class":"cover-buttons"})
    button_label = bs_obj.find("span",{"class":"button-label"})
    location = button_label.text

    lis = cover_button.findAll("li")
    #구조가 div안에 ul, li구조로 되어있고 li가 여러개이므로 findAll을 해준다.
    li_tag = lis[1]
    a_tag = li_tag.find("a")
    link = a_tag['href']

    dictionary1 = {}
    dictionary1['name'] = bp_name
    dictionary1['location'] = location
    dictionary1['link'] = link

    return dictionary1

url = "https://bp.eosgo.io/"

result = requests.get(url=url)

bs_obj = BeautifulSoup(result.content, "html.parser")
If_items = bs_obj.findAll("div",{"class":"lf-item"})
# <div class = "lf-item">으로 시작하는 결과를 뽑음
#.findAll을 이용했기 때문에 위 url의 모든 bp의 <div class = "lf-item">이 나옴

hrefs = [div.find("a")['href'] for div in If_items]
#If_items에 있는것을 div로 뽑아서 div안에 있는 a태그를 찾아 거기에 있는 href속성을 뽑아 다시 list로 만듬
#len(hrefs)를 하면 개수를 셀수가 있다.

for number in range(0,5) :
    dic_result = get_bp_info(hrefs[number])
    print(dic_result)