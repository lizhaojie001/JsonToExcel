#!/usr/bin/python3
 
import simplejson
import xlwt
import os
from openpyxl import load_workbook

# Python 字典类型转换为 JSON 对象

json = '{"versions":[{"version":"1.35.0","count":134},{"version":"1.36.0","count":172},{"version":"1.39.0","count":7},{"version":"1.39.1","count":5},{"version":"1.39.3","count":18},{"version":"1.39.4","count":391},{"version":"1.50.0","count":1},{"version":"1.50.1","count":83},{"version":"1.51.0","count":44},{"version":"1.52.0","count":318},{"version":"2.0.0","count":172},{"version":"2.1.0","count":2259},{"version":"2.1.5","count":340},{"version":"2.1.8","count":1937},{"version":"2.2.0","count":4091},{"version":"2.2.5","count":2},{"version":"2.3.0","count":3},{"version":"2.3.3","count":284},{"version":"2.4.5","count":8164},{"version":"2.5.1","count":13}],"total":18438}' 
 
data2 = simplejson.loads(json)

path='./奔溃率.xlsx'
 	# 创建新的workbook（其实就是创建新的excel）
workbook = xlwt.Workbook(encoding= 'ascii')

    # 创建新的sheet表
worksheet = workbook.add_sheet("My new Sheet",cell_overwrite_ok=True )

    # 往表格写入内容
worksheet.write(0,0, "version")
worksheet.write(0,1, "users")
worksheet.write(0,2, "carshs")
worksheet.write(0,3, "rat")
    

    # 保存

if os.path.exists(path):
   f = open(path,'wb')
   pass


 
versions = data2["versions"]
print(versions)
i = 1
for version in versions:
	v = version["version"]
	worksheet.write(i,0,v)
	c = version["count"]
	worksheet.write(i,1,c)
	i += 1
	pass

workbook.save(path)