'''
Created on 20171110

@author: Administrator
'''
from urllib import request

from getdata.datastorage import Datastorage


class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
          return None
        fails = 0
        try:
          #获取会话指针
          connection = Datastorage().getconnection();
          with connection.cursor() as cursor:
            #创建sql
            sql = "insert into `url_record`(`urls`) values(%s)"
            cursor.execute(sql,url)
            connection.commit()
        finally:
          connection.close()
        #add this try code to create the blocking problem when the net is unstable
        while True:
          try:
            if fails >=5:
              break
            req = request.Request(url)
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
            req.add_header("Accept","*/*")
            req.add_header("X-Requested-With","XMLHttpRequest")
            req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
            req.add_header("Referer","https://mp.toutiao.com/profile_v2/articles/own")
            #req.add_header("Accept-Encoding","gzip, deflate, br")
            req.add_header("Accept-Language","zh-CN,zh;q=0.8")
            req.add_header("Cookie","_ba=BA0.2-20171027-5110e-DnqNqAiGyVHuQiscbojv; UM_distinctid=15f5c667ac972d-0a35f145570c1f-3b3e5906-100200-15f5c667aca755; uuid='w:a98c0b0da2d4454ca04fde003b300664'; sid_tt=c3356934dd7fdf3ad307a1e2ee0b8fa3; _ga=GA1.2.798317896.1509083737; _gid=GA1.2.163429252.1510457272; currentMediaId=; tt_webid=65221452735; sso_login_status=1; sessionid=64a7744d92fc2d3f11e4d10b3b593117; _mp_test_key_1=c97b0d9790e61433587fe4139d8e36bb; tt_im_token=1510458641212550591119740441277845768877732312344866698837068396; _ga=GA1.3.798317896.1509083737; _gid=GA1.3.163429252.1510457272; currentMediaId=51646880050")
            resp = request.urlopen(req,None,5)
            #data = json.loads(resp.read().decode("unicode-escape"))
            #data["data"]["count"]
            #print(data["message"])
            if resp.getcode() !=200:
              return None
            #print(resp.read().decode("unicode-escape"))
            return resp.read()
          except:
            fails +=1
            print("the net was unstable and we are tying again:",fails) 
          else:
            break
    
