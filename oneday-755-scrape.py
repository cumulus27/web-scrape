import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import time
import datetime


with open('name.txt') as name:
    namelist=name.readlines()
for i in range(len(namelist)):
    namelist[i]=namelist[i].strip()

if not os.path.exists("755-download"):
    os.mkdir("755-download")


inum=0
isnum=0
vnum=0
vsnum=0
day=6
now=time.time()
today=datetime.datetime.now()
today=today.strftime('%Y-%m-%d')
for nameId in namelist:
    print('Downloading {}\'s pictures and movies now...'.format(nameId))
    Turl="https://api.7gogo.jp/web/v2/talks/{}/posts".format(nameId)
    try:
        html=urlopen(Turl).read().decode('utf-8')
    except URLError:
        print("URLError!")
        print("From： {}".format(Turl))
    except Exception as e:
        print("Unknown error: {}".format(e))
        print("From： {}".format(Turl))
    if not os.path.exists("755-download/{}".format(nameId)):
        os.mkdir("755-download/{}".format(nameId))
    if not os.path.exists("755-download/{}/{}".format(nameId,today)):
        os.mkdir("755-download/{}/{}".format(nameId,today))
    if not os.path.exists("755-download/{}/{}/videos".format(nameId,today)):
        os.mkdir("755-download/{}/{}/videos".format(nameId,today))
    if not os.path.exists("755-download/{}/{}/images".format(nameId,today)):
        os.mkdir("755-download/{}/{}/images".format(nameId,today))
    jsonHtml=json.loads(html)
    isnum=0
    vsnum=0
    for dataList in jsonHtml.get('data'):
        onePost=dataList.get('post')
        postTime=onePost.get('time')
        if now-postTime>86400*day:
            break
        for bodyList in onePost.get('body'):
            #download images
            url=bodyList.get('image')
            if url:
                info=url.split('/')
                imgtype=info[-1].split('.')
                if imgtype[-1]=='jpg':  #ignore png
                    for i in range(3):
                        del info[0]
                    link='-'
                    filename=link.join(info)
                    try:
                        urlretrieve(url,"755-download/{}/{}/images/{}".format(nameId,today,filename))
                    except URLError:
                        print("URLError!")
                        print("From： {}".format(url))
                    except Exception as e:
                        print("Unknown error: {}".format(e))
                        print("From： {}".format(url))
                    inum=inum+1
                    isnum=isnum+1
                    print(url)
            #download videos
            url=bodyList.get('movieUrlHq')
            if url:
                info=url.split('/')
                imgtype=info[-1].split('.')
                if 1==1:
                    for i in range(3):
                        del info[0]
                    link='-'
                    filename=link.join(info)
                    try:
                        urlretrieve(url,"755-download/{}/{}/videos/{}".format(nameId,today,filename))
                    except URLError:
                        print("URLError!")        
                        print("From： {}".format(url))
                    except Exception as e:
                        print("Unknown error: {}".format(e))
                        print("From： {}".format(url))                    
                    vnum=vnum+1
                    vsnum=vsnum+1
                    print(url)
    print("Download {} pictures and {} videos from {}".format(isnum,vsnum,nameId))
    if isnum==0:
        os.rmdir("755-download/{}/{}/images".format(nameId,today))
    if vsnum==0:
        os.rmdir("755-download/{}/{}/videos".format(nameId,today))
    if vsnum==0 and isnum==0:
        os.rmdir("755-download/{}/{}".format(nameId,today))
print("Download {} pictures and {} videos in all".format(inum,vnum))
