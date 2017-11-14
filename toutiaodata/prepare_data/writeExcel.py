'''
Created on 2017年11月14日
@author: Administrator
'''
import xlwt

from getdata.datastorage import Datastorage

f = xlwt.Workbook() #创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
row0 = [u'编号',u'标题',u'摘要',u'作者',u'发布日期',u'推荐',u'阅读',u'评论',u'涨粉',u'转发',u'收藏',u'系统参数1',u'系统参数2']
#生成第一行
for i in range(0,len(row0)):
  sheet1.write(0,i,row0[i])

print("start write data started……")
connection = Datastorage().getconnection()
try:
  #获取会话指针
  with connection.cursor() as cursor:
    #创建sql
    sql = "select * from `toutiao` where `id` is not null"
    count = cursor.execute(sql)
    print(count)
    #a =  cursor.fetchone()
    #print(a)
    #cursor.fetchmany(size = 1)
    all = cursor.fetchall()
    for i in range(0,count):
      for j in range(0,len(row0)):
        sheet1.write(i+1,j,all[i][j])
    connection.commit()
finally:
  connection.close()
    #数据字段13
    #获取第一个工作表
f.save('demo11.xlsx') #保存文件
print("writing datas ended……")