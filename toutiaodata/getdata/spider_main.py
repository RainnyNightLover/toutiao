'''
Created on 20171110
Administrator
'''
from getdata import html_downloader, datastorage


class SpiderMain(object):

    
    def __init__(self):
        #self.urls = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader()
        self.datastorage = datastorage.Datastorage()
        #give back parameters for looping
        
        
        
        
       # self.parser = html_parser.HtmlParser()
        #self.outputer = html_outputer.HtmlOutputer()
        
    def craw(self, root_url):
        count = 1
        #self.urls.add_new_url(root_url)
        while True:
          try:
            #new_url = self.urls.get_new_url()
            #print 'craw %d : %s' %(count, new_url)
            json_cont = self.downloader.download(root_url)
            modify_time, item_id ,date_time = self.datastorage.datadel(json_cont)
            #print(html_cont)
            #new_urls, new_data = self.parser.parser(new_url, html_cont)
            #self.urls.add_new_urls(new_urls)
            #self.outputer.collect_data(new_data)
            if count == 2:
              break
            count = count +1
          except:
            print('craw failed')
        #self.outputer.output_html()
        print("the end")
    
if __name__== "__main__":
  root_url = "https://mp.toutiao.com/core/article/media_article_list/?count=40&source_type=0&status=all&from_time=0&item_id="
  obj_spider = SpiderMain()
  obj_spider.craw(root_url)