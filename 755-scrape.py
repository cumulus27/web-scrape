from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


html=urlopen("https://api.7gogo.jp/web/v2/talks/hori-miona/posts").read().decode('utf-8')

jsonHtml=json.loads(html)
for dataList in jsonHtml.get('data'):
    for bodyList in dataList.get('post').get('body'):
        url=bodyList.get('image')
        if url:
            info=url.split('/')
            imgtype=info[-1].split('.')
            if imgtype[-1]=='jpg':
                for i in range(3):
                    del info[0]
                link='-'
                filename=link.join(info)
                urlretrieve(url,"images/image_"+filename)
                print(url)
