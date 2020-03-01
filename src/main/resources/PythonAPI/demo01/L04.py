import openpyxl as workbook

# 无代码提示
# openpyxl尝鲜
# 1.加载工作簿
wb = workbook.load_workbook(r"xxx.xlsx")
# 2.获取工作表
print(wb.sheetnames)
