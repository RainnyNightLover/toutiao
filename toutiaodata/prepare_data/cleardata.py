'''
Created on 2017年11月15日
@author: Administrator
'''
import re

from getdata.datastorage import Datastorage

print("start write data started……")
connection = Datastorage().getconnection()
try:
  #获取会话指针
  with connection.cursor() as cursor:
    #创建sql
    sql = "select `id` ,`abstract` from `toutiao` where `id` is not null"
    cursor.execute(sql)
    alldatas = cursor.fetchall()
    for data in alldatas:
      print(data)
      print(data[0])
      print(data[1])
      authors = re.findall(".*记者\s*(.+?)\s*\)",data[1])
      if authors:
        sql1 = "update toutiao set author = %s where id = %s"
        cursor.execute(sql1,(authors[0],data[0]))
        connection.commit()
        continue
      else:
        authors = re.findall(".*记者\s*(.+?)\s*）",data[1])
        if authors:
          sql1 = "update `toutiao` set `author` = %s where `id` = %s"
          print(authors[0])
          print(data[0])
          cursor.execute(sql1,(authors[0],data[0]))
          connection.commit()
        else:
          continue
  connection.commit()
finally:
  connection.close()