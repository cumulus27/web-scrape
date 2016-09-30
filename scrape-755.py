#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Main function
"""

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import time
import datetime

class Crawl:
    """
    Crawl the url of phote and video
    """
    def __init__(self,name_id,day_limit):
        self.now=time.time()
        self.time_limit=day_limit*86400
        self.url="https://api.7gogo.jp/web/v2/talks/{}/posts".format(name_id)
        try:
            html=urlopen(self.url).read().decode('utf-8')
        except Exception as e:
            print("Unknown error: {}".format(e))
            print("From： {}".format(self.url))
        self.json_data=json.loads(html)
        self.image_url=[]
        self.video_url=[]

    def get_url(self):
        for dataList in jsonHtml.get('data'):
            onePost=dataList.get('post')
            postTime=onePost.get('time')
            if now-postTime>self.time_limit:
                break
            for bodyList in onePost.get('body'):
                #get image url
                url=bodyList.get('image')
                if url:
                    info=url.split('/')
                    imgtype=info[-1].split('.')
                    if imgtype[-1]=='jpg':
                        self.image_url.append(url)
                #get video url
                url=bodyList.get('movieUrlHq')
                if url:
                    self.video_url.append(url)
        return self.image_url,self.video_url


class Download_url:
    """
    Download things from url
    """
    def __init__(self,name_id,url,ftype):
        today=datetime.datetime.now()
        today=today.strftime('%Y-%m-%d')
        if not os.path.exists("755-download/{}/{}/{}".format(name_id,today,ftype)):
            os.mkdirs("755-download/{}/{}/{}".format(name_id,today,ftype))
        self.path="755-download/{}/{}/{}/".format(name_id,today,ftype)
        self.urls=url

    def download(self):
        for url in self.urls:
            info=url.split('/')
            for i in range(3):
                del info[0]
            link='-'
            filename=link.join(info)
            try:
                urlretrieve(url,path+filename)
            except Exception as e:
                print("Unknown error: {}".format(e))
                print("From： {}".format(url))

if __name__ == '__main__':
    day_limit=1
    with open('name.txt') as name:
        namelist=name.readlines()
    for i in range(len(namelist)):
        namelist[i]=namelist[i].strip()

    for name_id in namelist:
        print('Downloading {}\'s pictures and movies now...'.format(name_id))
        my_crawl=Crawl(name_id,day_limit)
        [image_url,vedio_url]=my_crawl.get_url()
        image_dl=Download_url(image_url,'image')
        image_dl.download()
        video_dl=Download_url(video_url,'video')
        image_dl.download()
        
        
        
