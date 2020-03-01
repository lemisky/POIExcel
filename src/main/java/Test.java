import org.apache.poi.hssf.usermodel.HSSFSheet;
import org.apache.poi.hssf.usermodel.HSSFWorkbook;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.Row;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Iterator;

public class Test {
    /**
     * python数据处理，自动化办公网上传的很火
     * 但是自己使用了一下，感觉很难用，没有代码提示，
     * 可能是我对python不够熟悉吧，感觉java更方便
     * <p>
     * 下面演示一个小例子
     */
    public static void main(String[] args) throws IOException {
        //读取工作簿文件
        HSSFWorkbook workbook = new HSSFWorkbook(new FileInputStream("xxx.xls"));
        //获取第一个工作表
        HSSFSheet sheet = workbook.getSheetAt(0);
        //获取表名
        System.out.println(sheet.getSheetName());

        //遍历工作表
        //第一种方式:迭代器
        //取每行的迭代器
        Iterator<Row> rowIterator = sheet.rowIterator();
        while (rowIterator.hasNext()) {
            Row next = rowIterator.next();
            //取每个单元格的迭代器
            Iterator<Cell> cellIterator = next.cellIterator();
            while (cellIterator.hasNext()) {
                Cell cell = cellIterator.next();
                //如果时字符串数据就打印出来
                System.out.print(cell);
//                if (cell.getCellType() == CellType.STRING)
//                    System.out.print(cell.getStringCellValue() + "\t");
            }
            System.out.println();
        }

    }

}
