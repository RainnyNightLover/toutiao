'''
Created on 20171110
Administrator
'''
from operator import le

from getdata import html_downloader, datastorage

class SpiderMain(object):

    def __init__(self):
        self.downloader = html_downloader.HtmlDownloader()
        self.datastorage = datastorage.Datastorage()
    def craw(self,url,date):
        count = 1
        flag = True
        while flag:
          try:
            json_cont = self.downloader.download(url)
            print(json_cont)
            #used to form the next url to get data
            modify_time, item_id ,date_time = self.datastorage.datadel(json_cont)
            print(modify_time, item_id ,date_time)
            url = "https://mp.toutiao.com/core/article/media_article_list/?count=10&source_type=0&status=passed&from_time=%s&item_id=%s" %(modify_time, item_id)
            print(url)
            flag = le(date,date_time)
            #flag = False
          except:
            print('craw failed')
        #self.outputer.output_html()
        print("the end")
    
if __name__== "__main__":
  root_url = "https://mp.toutiao.com/core/article/media_article_list/?count=20&source_type=0&status=passed&from_time=0&item_id="
  obj_spider = SpiderMain()
  #input the date which startpoint u what to start
  obj_spider.craw(root_url,"2017-11")