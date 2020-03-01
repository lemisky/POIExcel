import xlrd
import xlutils.copy
import xlwt


# 自定义处理数据函数
def deal_value(cell):
    if cell.ctype == xlrd.XL_CELL_EMPTY or len(cell.value) == 0:
        return cell.value
    else:
        string = cell.value
        return ("{\"Url\":\"https://www.fanyouvip.com/DownLoad/" +
                string +
                "\",\"Name\":\"" +
                string[string.index("_") + 1:] +
                "\"}")


# 1.使用xlrd读取工作簿
book = xlrd.open_workbook(r"xxx.xls", formatting_info=True,
                          on_demand=True)

# 2.使用xlutils转xlrd工作簿对象为xlwt工作簿对象
# 此处返回xlwt对象
wb = xlutils.copy.copy(book)

# 3.获取工作表对象
ws = wb.get_sheet(0)  # type: xlwt.Worksheet
# 4.读取并修改数据
sheet = book.sheet_by_index(0)
n = 1
while n < sheet.nrows:
    ws.write(n, 5, deal_value(sheet.row(n)[5]))
    ws.write(n, 6, deal_value(sheet.row(n)[6]))
    n += 1

# 5.保存
wb.save("xlutils.xls")
print("处理完毕！")
