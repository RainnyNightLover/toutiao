'''
Created on 2017年11月13日

@author: Administrator
'''
import json

from pip._vendor.appdirs import unicode
import pymysql


class Datastorage(object):
    #获取数据库连接
    def getconnection(self):
      connection = pymysql.connect(host = "172.16.90.55",
                                 user = "root",
                                 password = "root",
                                 db = "spider",
                                 charset = "utf8mb4"
                                 )
      return connection
    
    def datadel(self,json_cont):
      text = unicode( json_cont, errors='ignore')
      data = json.loads(text)
      i = 0
      for data_detail in data["data"]["articles"]:
        try:
          #获取会话指针
          print(data_detail)
          connection = self.getconnection();
          with connection.cursor() as cursor:
            #创建sql
            sql = "insert into `toutiao`(`title`,`abstract`,`pass_time`,`impression_count`,`go_detail_count`,`comment_count`,`subscribe_count`,`share_count`,`favorite_count`,`item_id`,`modify_time`) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,(data_detail["title"],data_detail["abstract"],data_detail["pass_time"],data_detail["impression_count"],data_detail["go_detail_count"],data_detail["comment_count"],data_detail["subscribe_count"],data_detail["share_count"],data_detail["favorite_count"],data_detail["item_id"],data_detail["modify_time"]))
            connection.commit()
        finally:
          connection.close()
        i = i+1
        print(i)
        date = data_detail["pass_time"][0:7]
      return data_detail["modify_time"],data_detail["item_id"],date
        



