import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0'}


def get_page_products(url):
    result = requests.get(url,headers=headers)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul",{"class":"prdList column5"})
    boxes = ul.findAll("div", {"class":"box"})
    product_info_list = [get_product_info(box) for box in boxes]

    return product_info_list


def get_product_info(box):
    ptag = box.find("p",{"class":"name"})
    spans_name = ptag.findAll("span")
    ul = box.find("ul", {"class": "xans-element- xans-product xans-product-listitem"})
    spans_price = ul.findAll("span")
    a = box.find("a")
    link = a['href']

    name = spans_name[1].text
    price = spans_price[1].text

    return {"name":name,"price":price,"link":link}

urls =["http://jolse.com/category/tonermist/43/?page=1",
        "http://jolse.com/category/tonermist/43/?page=2",
       "http://jolse.com/category/tonermist/43/?page=3",
       "http://jolse.com/category/tonermist/43/?page=4",
       "http://jolse.com/category/tonermist/43/?page=5"
]

for page_number in range(0, 5):
    page_products = get_page_products(urls[page_number])
    print(len(page_products),page_products)
