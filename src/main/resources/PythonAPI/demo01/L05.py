import xlsxwriter

# 有完整的代码提示
wb = xlsxwriter.Workbook(r"xxx.xlsx")
ws = wb.add_worksheet("sheet1")
ws.write_string(0, 0, "hello xlsWriter")
wb.close()
