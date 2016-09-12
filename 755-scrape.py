from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


html=urlopen("https://api.7gogo.jp/web/v2/talks/hori-miona/posts").read().decode('utf-8')

jsonHtml=json.loads(html)
for dataList in jsonHtml.get('data'):
    for bodyList in dataList.get('post').get('body'):
        url=bodyList.get('image')
        print('get one')
        if url:
            info=url.split('/')
            filename=info[-1]
            urlretrieve(url,"images/"+filename)
            print(url)
