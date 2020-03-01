# xlrd读取工作簿
import xlrd

# 1.打开工作簿
book = xlrd.open_workbook(r"xxx.xls")
# 2.获取工作表
ws = book.sheet_by_index(0)
# 3.遍历一下
for row in ws.get_rows():
    print(row[0].value)
