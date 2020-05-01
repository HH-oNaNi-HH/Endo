import requests
from bs4 import BeautifulSoup
from enum import Enum
class InvInfo(Enum):
    exists = 1
    not_exists = 2
    error = 3

url = 'https://lohaco.jp/product/E415123/?int_id=search_categorys' #後でUIから入力させる。
headers = {'User-Agent':'Mozilla/5.0'}
soup = BeautifulSoup(requests.get(url,headers=headers).content,'html.parser')

member = ''
exists = 0

for div in soup.find_all('div',class_='blcStockInfo'):
    exists = InvInfo.not_exists
    for p in div.find_all('p',class_='elmInStock elmTxt'):
        exists = InvInfo.exists

print(exists)
