import xlwt

# 1.创建工作簿
wb = xlwt.Workbook()
# 2.添加工作表
# 无法识别类型，进行代码提示，手动添加类型识别代码
ws = wb.add_sheet("sheet1")  # type: xlwt.Worksheet
# 3.写入数据
ws.write(0, 0, "第一行第一列")
ws.write(0, 1, "第一行第二列")
# 4.保存数据
wb.save("xlwt.xls")

