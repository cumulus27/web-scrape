import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

name=open('name.txt')
namelist=name.readlines()
for i in range(len(namelist)):
    namelist[i]=namelist[i].strip()


num=0
snum=0
for nameId in namelist:
    print('Downloading {}\'s picture now...'.format(nameId))
    Turl="https://api.7gogo.jp/web/v2/talks/{}/posts".format(nameId)
    html=urlopen(Turl).read().decode('utf-8')
    if not os.path.exists("images/{}".format(nameId)):
        os.mkdir("images/{}".format(nameId))

    jsonHtml=json.loads(html)
    snum=0
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
                    urlretrieve(url,"images/{}/image-{}".format(nameId,filename))
                    num=num+1
                    snum=snum+1
                    print(url)
    print("Download {} pictures from {}".format(snum,nameId))
print("Download {} pictures in all".format(num))
