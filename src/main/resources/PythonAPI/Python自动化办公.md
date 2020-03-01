# Python自动化办公

## 入门概述

1. xlrd只能读取工作簿
2. xlwt只能重新创建写入
3. xlutils整合xlrd和xlwt，用于追加
4. 在安装包时，只需 **pip3 install xlutils** 即可，会自动安装xlrd和xlwt

### xlrd读取工作簿

```python
# xlrd读取工作簿
import xlrd

# 1.打开工作簿
book = xlrd.open_workbook(r"D:\Users\foyou\HBuilderX\Projects\PythonAPI\test2.xls")
# 2.获取工作表
ws = book.sheet_by_index(0)
# 3.遍历一下
for row in ws.get_rows():
    print(row[0].value)

```

### xlwt写入数据

```python
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

```

### xlutils数据追加

```python
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
book = xlrd.open_workbook(r"D:\Users\foyou\HBuilderX\Projects\PythonAPI\test2.xls", formatting_info=True,
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

```

### 使用体验

- **个人感觉不咋样，代码提示很有问题**

### openpyxl

```python
import openpyxl as workbook

# 无代码提示
# openpyxl尝鲜
# 1.加载工作簿
wb = workbook.load_workbook(r"D:\Users\foyou\HBuilderX\Projects\PythonAPI\test1.xlsx")
# 2.获取工作表
print(wb.sheetnames)

```

### xlswriter

```python
import xlsxwriter

# 有完整的代码提示
wb = xlsxwriter.Workbook(r"D:\Users\foyou\HBuilderX\Projects\PythonAPI\demo01\test002.xlsx")
ws = wb.add_worksheet("sheet1")
ws.write_string(0, 0, "hello xlsWriter")
wb.close()

```

